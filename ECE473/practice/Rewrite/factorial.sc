(define (my-if p q r) (if p q r))

(define (factorial n)
 (if (zero? n)
     1
     (* n (factorial (- n 1)))))

{ int x = 42;
      { int x = 43;
	    ... x ...
	    }
      ... x ...
      }
