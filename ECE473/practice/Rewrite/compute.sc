;;; (compute expression environment definitions) ===> value

;;; A value is a number.
;;; A variable is a symbol.
;;; An expression is
;;; - a value,
;;; - a variable,
;;; - (+ e1 ... en), where e1, ..., en are expressions,
;;; - (- e1 e2 ... en), where e1, ..., en are expressions,
;;; - (* e1 ... en), where e1, ..., en are expressions,
;;; - (/ e1 e2 ... en), where e1, ..., en are expressions,
;;; - (sqrt e), where e is an expression,
;;; - (expt e1 e2), where e1 and e2 are expressions,
;;; - (if e1 e2 e3), where e1, e2, and e3 are expressions,
;;; - (derivative e), where e is an expression, or
;;; - (f e1 ... en), where f is a function name and e1, ..., en are expressions,
;;; A definition is
;;; - (define (f x1 ... xn) e), where f is a function name, x1, ..., xn are
;;;   variables, and e is an expression.
;;; A binding is (x v) where x is a variable and v is a value.
;;; An environment is a list of bindings.

(define (lookup variable environment)
 (cond ((null? environment) (panic "Unbound variable"))
       ((eq? (first (first environment)) variable) (second (first environment)))
       (else (lookup variable (rest environment)))))

(define (lookup-definition function-name definitions)
 (cond ((null? definitions) (panic "Undefined function-name"))
       ((eq? (first (second (first definitions))) function-name)
	(first definitions))
       (else (lookup-definition function-name (rest definitions)))))

(define (make-environment variables values)
 (if (null? variables)
     (if (null? values)
	 '()
	 (panic "Too many arguments"))
     (if (null? values)
	 (panic "Too few arguments")
	 (cons (list (first variables) (first values))
	       (make-environment (rest variables) (rest values))))))

(define (compute e environment definitions)
 (define (compute-with-environment e) (compute e environment definitions))
 (cond
  ((number? e) e)
  ((symbol? e) (lookup e environment))
  ((list? e)
   (if (null? e)
       (panic "invalid expression")
       (case (first e)
	((+) (map-reduce + 0 compute-with-environment (rest e)))
	((-) (case (length (rest e))
	      ((0) (panic "- must take one or more arguments"))
	      ((1) (- (compute-with-environment (second e))))
	      (else (+ (compute-with-environment (second e))
		       (- (map-reduce
			   + 0 compute-with-environment (rest (rest e))))))))
	((*) (map-reduce * 1 compute-with-environment (rest e)))
	((/) (case (length (rest e))
	      ((0) (panic "/ must take one or more arguments"))
	      ((1) (/ (compute-with-environment (second e))))
	      (else (* (compute-with-environment (second e))
		       (/ (map-reduce
			   * 1 compute-with-environment (rest (rest e))))))))
	((sqrt) (if (= (length (rest e)) 1)
		    (sqrt (compute-with-environment (second e)))
		    (panic "sqrt must take exactly one argument")))
	((expt) (if (= (length (rest e)) 2)
		    (expt (compute-with-environment (second e))
			  (compute-with-environment (third e)))
		    (panic "expt must take exactly two arguments")))
	((agar) (if (= (length (rest e)) 3)
		    (if (zero? (compute-with-environment (second e)))
			(compute-with-environment (third e))
			(compute-with-environment (fourth e)))
		    (panic "if must take exactly three arguments")))
	((derivative) (if (= (length (rest e)) 1)
			  (compute-with-environment (derivative (second e)))
			  (panic "derivative must take exactly one argument")))
	(else (let* ((function-name (first e))
		     (definition (lookup-definition function-name definitions))
		     (values (map compute-with-environment (rest e)))
		     (variables (rest (second definition)))
		     (environment (make-environment variables values))
		     (body (third definition)))
	       (compute body environment definitions))))))
  (else (panic "invalid expression"))))
