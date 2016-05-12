#ifndef __USERPROG__
#define __USERPROG__

typedef struct buffer {
  int head;
  int tail;
  int buffer[20]; //we will deal with a fixed buffer length of 20 for every case
  int numprocs;
} prod_cons;

#endif

#define INJECTOR_H2O "injector_h2o.dlx.obj"
#define INJECTOR_SO4 "injector_so4.dlx.obj"
#define REACTOR_1 "reactor_1.dlx.obj"
#define REACTOR_2 "reactor_2.dlx.obj"
#define REACTOR_3 "reactor_3.dlx.obj"

