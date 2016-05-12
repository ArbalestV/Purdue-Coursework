struct int_list {
  int first;
  struct int_list *rest;
}

int reduce(int (*f)(int, int), struct int_list *l, int i) {
  if (l==NULL) return i;
  else return (*f)(l->first, reduce(f, l->rest, i));
}
