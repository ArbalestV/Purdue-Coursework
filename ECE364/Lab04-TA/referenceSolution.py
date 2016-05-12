from pprint import pprint as pp

def loadPermissions():
    # return the list of users and permissions from the permissions file.
    with open("Permissions.txt", "r") as permissionFile:
        permissions = permissionFile.readlines()[2:]

    permissionList = [[i.strip() for i in permission.split(":")]
                      for permission in permissions]

    return permissionList


def loadUsers():
    # Return a dictionary that maps user IDs to user names.

    with open("Users.txt", "r") as usersFile:
        users = usersFile.readlines()[2:]
        userList = [user.split("|") for user in users]

    userMap = {userID.strip(): userName.strip() for userName, userID in userList}

    return userMap


def parseLogFile():
    # return a list of entries from the log. Each entry is the tuple (userID, url, controller, action, accessGranted).

    with open("ActivityLog.txt", "r") as logFile:
        entries = logFile.readlines()
        logEntries = [entry.strip().split(" : ") for entry in entries]

    logTuples = []
    for userID, url in logEntries:
        isAccessGranted = canGrantAccess(userID, url)
        _, _, _, controller, action = url.split("/")
        entry = userID, url, controller, action, isAccessGranted
        logTuples.append(entry)

    return logTuples


def getUserPermissions():
    # return a {string: set} dictionary of the user ID, and the controllers he/she can access.
    permissionList = loadPermissions()
    permissionMap = {}

    for userID, controller in permissionList:

        if userID not in permissionMap.keys():
            permissionMap[userID] = {controller}
        else:
            controllerSet = permissionMap[userID]
            controllerSet.add(controller)

    return permissionMap


def getControllerPermissions():
    # return a {string: set} dictionary of the controller, and the set of users that can access it.

    permissionList = loadPermissions()
    userMap = loadUsers()
    permissionMap = {}

    for userID, controller in permissionList:
        userName = userMap[userID]

        if controller not in permissionMap.keys():
            permissionMap[controller] = {userName}
        else:
            userSet = permissionMap[controller]
            userSet.add(userName)

    return permissionMap


def getControllerActions():
    # return a {string: set} dictionary of the controller, and the set of actions requested in that controller in the
    # log.

    logEntries = parseLogFile()
    actionMap = {}

    for _, _, controller, action, _ in logEntries:

        if controller not in actionMap.keys():
            actionMap[controller] = {action}
        else:
            actionSet = actionMap[controller]
            actionSet.add(action)

    return actionMap


def canGrantAccess(userID, url):
    # return true if the given user can access the URL.

    userPermissions = getUserPermissions()

    if userID not in userPermissions.keys():
        return False

    permissionSet = userPermissions[userID]
    controller = url.split("/")[3]

    return controller in permissionSet


def checkUserActivity(userID):
    # return a list of (string, bool) tuples, where the first is the URL accessed by the user, and the second is whether
    # the user has been granted access to that URL or not.

    logEntries = parseLogFile()
    userActivity = [(url, isAccessGranted)
                    for ID, url, _, _, isAccessGranted in logEntries
                    if userID == ID]

    return userActivity


def getActivityByUser():
    # return a dictionary containing {string: (int, int)} where the key is the user Name, and the value is a tuple
    # containing the number of pages with granted access and the number of pages with denied access.

    logEntries = parseLogFile()
    userMap = loadUsers()
    activityByUser = {}

    for userID, userName in userMap.items():

        entries = [isAccessGranted for ID, _, _, _, isAccessGranted in logEntries if userID == ID]
        activityByUser[userName] = (entries.count(True), entries.count(False))

    return activityByUser


def getActivityByController():
    # return a dictionary containing {string: (int, int)} where the key is the controller, and the value is a tuple
    # containing the number of pages with granted access and the number of pages with denied access.

    logEntries = parseLogFile()
    controllers = set([controller for _, controller in loadPermissions()])

    activityByController = {}

    for controller in controllers:
        entries = [isAccessGranted for _, _, ctrl, _, isAccessGranted in logEntries if controller == ctrl]
        activityByController[controller] = (entries.count(True), entries.count(False))

    return activityByController


# def getActivityByAction():
#     # return a dictionary containing {string: (int, int)} where the key is the action, and the value is a tuple
#     # containing the number of times with granted access and the number of times with denied access.
#
#     logEntries = loadLog()
#     actions = set([action for _, _, _, action, _ in logEntries])
#
#     activityByAction = {}
#
#     for action in actions:
#         entries = [isAccessGranted for _, _, _, act, isAccessGranted in logEntries if action == act]
#         activityByAction[action] = (entries.count(True), entries.count(False))
#
#     return activityByAction

if __name__ == "__main__":
    # logEntries = parseLogFile()
    # pp(logEntries)

    # userPermissions = getUserPermissions()
    # pp(userPermissions)

    # controllerPermissions = getControllerPermissions()
    # pp(controllerPermissions)

    # controllerActions = getControllerActions()
    # pp(controllerActions)

    # user1Activity = checkUserActivity("jevans")
    # user1Activity.sort()
    # pp(user1Activity)
    #
    # user2Activity = checkUserActivity("sward")
    # user2Activity.sort()
    # pp(user2Activity)
    #
    activityByUser = getActivityByUser()
    pp(activityByUser)

    activityByController = getActivityByController()
    pp(activityByController)

