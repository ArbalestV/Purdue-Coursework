1. one-level - 
Checked with examle-paging test case.
- In makeprocs.c, because the user process exits simulation in the first process due to illegal access, it wouldn't get to the second process. So to work around that, just replace the first process name with the second process name, and it will give you an illegal access error for the second test file too. All in all, it works fine (illegal access on your provided test files).
By default, it will run test1.c.

2. User Test Programs - 
- Checked by both running them together, as well as individually. Please note the following conventions for testing different functionalities - 
(a) program to print hello world is called "step1" - the first program that is run.
(b) program to index outside of the virtual address space, and therefore generate an illegal access which exits the simulator (placed last in makeprocs.c), is called "step2".
(c) program to generate segmentation fault for accessing memory inside of the virtual address space but outside the currently allocated pages is called "step3" (run second in makeprocs.c).
(d) program that allocates multiple stack frames is called "step4" (run third in makeprocs.c). I would suggest running it by itself in order to see the full extent of allocation of new pages. The print statements are very descriptive.
(e) program that prints 100 instances of "hello_world.c" is placed fourth within the order of process listings in makeprocs.c, and it just called hello_world.c in a for loop.
(f) Lastly, spawning 30 processes counting on a large number within a loop to show interleaving within processes is placed fifth in makeprocs.c, and the print statements suggest when they are getting in and getting out of the processes. You can see a decent amount of interleaving. 
NOTE - There is some synchonizaion issue due to which the very last line of a few of the spawned processes may not be printed out because the illegal access program (step2.c) is called right after and the simulator exits. However if you comment out the illegal access generating program, you will see all the statements of all the spawned processes ae being printed. I discussed this with the GTA Venkat, he said that must be a synchronization issue and ma have nothing to do with the OS.
By default, makeprocs.c is running all the programs that we were supposed to test our OS on.

3. 2-Level Paging - 
Testing done same as one-level. No real difference. Please apply whatever was written for one-level to test 2-level. By default, "step2.c" is commented out because without that spawned processes do not run to completion. But I believe this is another synchronization problem. You can comment in and comment out individual programs to test their functionalities.
NOTE - A couple of extra debugging statements printing the stack address and the fauling address are being printed to show when to produce a segmentation fault and when to allocate one more page on the user stack. The GTAs can remove them from the pageFaultHandler() function if they so please. 


4. Heap management - 
Everything done as suggested, the print statements are formatted in the way requested. The output(s) match the gold output(s).


 

