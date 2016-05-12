;;; (simplify expression) ===> simple expression

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
;;; A calculable expression  is
;;; - a value,
;;; - (+ e1 ... en), where e1, ..., en are calculable expressions,
;;; - (- e1 e2 ... en), where e1, ..., en are calculable expressions,
;;; - (* e1 ... en), where e1, ..., en are calculable expressions,
;;; - (/ e1 e2 ... en), where e1, ..., en are calculable expressions,
;;; - (sqrt e), where e is an calculable expression, or
;;; - (expt e1 e2), where e1 and e2 are calculable expressions.

(define (and-function p q) (and p q))

(define (calculable? e)
 (cond ((number? e) #t)
       ((symbol? e) #f)
       ((list? e) (reduce and-function (map calculable? (rest e)) #t))
       (else (panic "invalid expression"))))

(define (simplify e)
 (cond
  ((calculable? e) (calculate e))
  ((number? e) e)
  ((symbol? e) e)
  ((list? e)
   (if (null? e)
       (panic "invalid expression")
       (case (first e)
	((+) (case (length (rest e))
	      ((0) 0)
	      ((1) (simplify (second e)))
	      ((2) (let ((e1 (simplify (second e)))
			 (e2 (simplify (third e))))
		    (cond ((and (number? e1) (zero? e1)) e2)
			  ((and (number? e2) (zero? e2)) e1)
			  ((and (list? e2) (eq? (first e2) '+))
			   (simplify
			    (list '+
				  (list '+
					(second e)
					(second (third e)))
				  (third (third e)))))
			  (else (list '+ e1 e2)))))
	      (else (simplify (list '+ (second e) (cons '+ (rest (rest e))))))))
	((-) (case (length (rest e))
	      ((0) (panic "- must take one or more arguments"))
	      ((1) (simplify (list '* -1 (second e))))
	      (else (simplify
		     (list
		      '+ (second e) (list '- (cons '+ (rest (rest e)))))))))
	((*) (case (length (rest e))
	      ((0) 1)
	      ((1) (simplify (second e)))
	      ((2) (let ((e1 (simplify (second e)))
			 (e2 (simplify (third e))))
		    (cond ((and (number? e1) (zero? e1)) 0)
			  ((and (number? e2) (zero? e2)) 0)
			  ((and (number? e1) (= e1 1)) e2)
			  ((and (number? e2) (= e2 1)) e1)
			  ((and (list? e2) (eq? (first e2) '*))
			   (simplify
			    (list '*
				  (list '*
					(second e)
					(second (third e)))
				  (third (third e)))))
			  (else (list '* e1 e2)))))
	      (else (simplify (list '* (second e) (cons '* (rest (rest e))))))))
	((/) (case (length (rest e))
	      ((0) (panic "/ must take one or more arguments"))
	      ((1) (simplify (list 'expt (second e) -1)))
	      (else (simplify
		     (list
		      '* (second e) (list '/ (cons '* (rest (rest e)))))))))
	((sqrt) (if (= (length (rest e)) 1)
		    (simplify (list 'expt (second e) 0.5))
		    (panic "sqrt must take exactly one argument")))
	((expt) (if (= (length (rest e)) 2)
		    (let ((e1 (simplify (second e)))
			  (e2 (simplify (third e))))
		     (cond ((and (number? e1) (= e1 1)) 1)
			   ((and (number? e2) (= e2 1)) e1)
			   (else (list 'expt e1 e2))))
		    (panic "expt must take exactly two arguments")))
	(else (panic "invalid operator")))))
  (else (panic "invalid expression"))))