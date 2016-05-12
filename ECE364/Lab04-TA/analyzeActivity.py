#! /usr/local/bin/python3.4
__author__ = 'mzaim'


def parsePermissions ():
    #returns list of (user, permission) tuples
    permissionsList = []

    with open ("Permissions.txt", "r") as f:
        content = f.readlines()

    for line in content[2:]:
        user = line.split(":")[0].strip()
        permission = line.split (":")[1].strip()
        permissionsList.append ((user, permission))

    return permissionsList

def parseUsers ():
    # returns a dictionary of the format {userID : full name}
    usersDict = {}
    with open ("Users.txt", 'r') as f:
        content = f.readlines()

    for line in content[2:]:
        name, id = line.split("|")
        usersDict [id.strip()] = name.strip()

    return usersDict

def parseLogFile ():
    with open ("ActivityLog.txt", "r") as f:
        content = f.readlines()

    permissionsList = parsePermissions()
    logEntries = []
    for line in content:
        userID, url = line.split(" : ")
        _, _, _, controller, action = url.split ("/")
        actionPermission = canGrantAccess(userID, url)

        logEntry = (userID.strip(), url.strip(), controller, action.strip(), actionPermission)
        logEntries.append (logEntry)

    return logEntries

def getUserPermissions ():
    userPermissions = {}
    permissionsList = parsePermissions()

    for user, permission in permissionsList:
        if user not in userPermissions.keys():
            userPermissions [user] = set()
        userPermissions[user].add (permission)

    return userPermissions

def getControllerPermissions ():
    controllerPermissions = {}
    permissionsList = parsePermissions()
    usersDict = parseUsers ()

    for user, permission in permissionsList:
        if permission not in controllerPermissions.keys():
            controllerPermissions [permission] = set()
        controllerPermissions [permission].add (usersDict[user])

    return controllerPermissions

def checkUserActivity (userID):
    allLogEntries = parseLogFile()
    userLogEntries = []

    for id, url, _, _, permission in allLogEntries:
        if (id == userID):
            userLogEntries.append ((url, permission))

    return userLogEntries

def getActivityByUser ():
    allLogEntries = parseLogFile()
    usersDict = parseUsers ()

    allActivities = {}
    for userID, userName in usersDict.items():
        userLogEntries = checkUserActivity(userID)

        allowedCount = 0
        deniedCount = 0
        for _, permission in userLogEntries:
            if permission is True: allowedCount += 1
            elif permission is False: deniedCount += 1

        allActivities[userName] = (allowedCount, deniedCount)

    return allActivities

def getActivityByController ():
    allLogEntries = parseLogFile()
    controllerPermissions = getControllerPermissions()
    allActivities = {}

    for _, url, controller, _, permission in allLogEntries:
        if controller not in allActivities.keys():
            allActivities [controller] = [0, 0]

        if permission is True:
            allActivities [controller][0] = allActivities[controller][0] + 1
        elif permission is False:
            allActivities [controller][1] = allActivities[controller][1] + 1

    for key in allActivities.keys():
        allActivities[key] = tuple (allActivities[key])

    return allActivities

def getControllerActions ():
    controllerActions = {}
    allLogEntries = parseLogFile()
    for _, _, controller, action, _ in allLogEntries:
        if controller not in controllerActions:
            controllerActions[controller] = set()
        controllerActions[controller].add (action)

    return controllerActions

def canGrantAccess (userID, url):
    permissionsList = parsePermissions()
    controller = url.split("/")[-2]

    if (userID.strip(), controller) in permissionsList:
            return True
    else:
            return False

if __name__ == "__main__":
    parseLogFile()