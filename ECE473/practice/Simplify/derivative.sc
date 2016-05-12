;;; (derivative expression) ===> expression
;;; (simple-derivative simple-expression) ===> simple-expression

;;; A value is a number.
;;; A variable is a symbol.
;;; An expression is
;;; - a value,
;;; - a variable,
;;; - (+ e1 ... en), where e1, ..., en are expressions,
;;; - (- e1 e2 ... en), where e1, ..., en are expressions,
;;; - (* e1 ... en), where e1, ..., en are expressions,
;;; - (/ e1 e2 ... en), where e1, ..., en are expressions,
;;; - (sqrt e), where e is an expression, or
;;; - (expt e1 e2), where e1 and e2 are expressions.
;;; A simple expression is
;;; - a value,
;;; - a variable,
;;; - (+ e1 e2), where e1 and e2 are simple expressions,
;;; - (* e1 e2), where e1 and e2 are simple expressions,
;;; - (expt e1 e2), where e1 and e2 are simple expressions.

(define (simple-derivative e)
 (cond
  ((number? e) 0)
  ((symbol? e) (if (eq? e 'x) 1 0))
  ((list? e)
   (if (null? e)
       (panic "invalid expression")
       (case (first e)
	((+) (if (= (length (rest e)) 2)
		 (list '+
		       (simple-derivative (second e))
		       (simple-derivative (third e)))
		 (panic "+ must take exactly two arguments")))
	((*) (if (= (length (rest e)) 2)
		 (list '+
		       (list '*
			     (second e)
			     (simple-derivative (third e)))
		       (list '*
			     (third e)
			     (simple-derivative (second e))))
		 (panic "* must take exactly two arguments")))
	((expt) (if (= (length (rest e)) 2)
		    (if (number? (third e))
			(list '*
			      (third e)
			      (list '*
				    (list 'expt
					  (second e)
					  (- (third e) 1))
				    (simple-derivative (second e))))
			(panic "cannot (yet) handle nonnumeric exponents"))
		    (panic "expt must take exactly two arguments")))
	(else (panic "invalid operator")))))
  (else (panic "invalid expression"))))

(define (derivative e) (simplify (simple-derivative (simplify e))))
