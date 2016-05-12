int plus(int m, int n) {
  if (n==0) return m;
  else return plus(m, n-1)+1;
}

int plus(int m, int n) {
  if (n==0) return m;
  else return plus(m+1, n-1);
}

int plus(int m, int n) {
 l:
  if (n==0) return m;
  else {
    m = m+1;
    n = n-1;
    goto l;
  }
}
