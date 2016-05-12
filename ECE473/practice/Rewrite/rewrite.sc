;;; (rewrite expression rules) ===> expression

;;; A value is
;;; - a number or
;;; - a boolean.

;;; A variable is a symbol.

;;; An expression is
;;; - a value,
;;; - a variable, or
;;; - (e1 e2 ... en), where e1, e2, ..., en are expressions.

;;; An expression variable is e, e1, e2, ..., e6.

;;; An expression pattern is
;;; - an expression variable,
;;; - a value,
;;; - a variable, or
;;; - (e1 e2 ... en), where e1, e2, ..., en are expression patterns.

;;; A rule is (lhs -~-> rhs), where lhs and rhs are expression patterns.

;;; A binding is (p e) where p is an expression variable and e is an expression.

;;; (match pattern expression) ===> bindings or #f

(define (value? p) (or (number? p) (boolean? p)))

(define (variable? p) (symbol? p))

(define (expression-variable? p) (member p '(e e1 e2 e3 e4 e5 e6)))

(define (inconsistent? bindings1 bindings2)
 (some (lambda (binding1)
	(some
	 (lambda (binding2)
	  (and (eq? (first binding1) (first binding2))
	       (not (equal? (second binding1) (second binding2)))))
	 bindings2))
       bindings1))

(define (combine result1 result2)
 (if (or (eq? result1 #f) (eq? result2 #f) (inconsistent? result1 result2))
     #f
     (append result1 result2)))

(define (match p e)
 (cond ((expression-variable? p) (list (list p e)))
       ((value? p) (if (equal? p e) '() #f))
       ((variable? p) (if (equal? p e) '() #f))
       ((list? p)
	(if (and (list? e) (= (length p) (length e)))
	    (map-reduce combine '() match p e)
	    #f))
       (else (panic "Invalid pattern"))))

;;; (instantiate p bindings) ===> expression

(define (lookup variable bindings)
 (cond ((null? bindings) (panic "Unbound variable"))
       ((eq? (first (first bindings)) variable) (second (first bindings)))
       (else (lookup variable (rest bindings)))))

(define (instantiate p bindings)
 (cond ((expression-variable? p) (lookup p bindings))
       ((value? p) p)
       ((variable? p) p)
       ((list? p) (map (lambda (p) (instantiate p bindings)) p))
       (else (panic "Invalid pattern"))))

(define (find-matching-rule e rules)
 (cond ((null? rules) #f)
       ((not (eq? (match (first (first rules)) e) #f)) (first rules))
       (else (find-matching-rule e (rest rules)))))

(define (rewrite e rules)
 (let* ((e (if (list? e) (map (lambda (e) (rewrite e rules)) e) e))
	(rule (find-matching-rule e rules)))
  (if (eq? rule #f)
      e
      (rewrite (instantiate (third rule) (match (first rule) e)) rules))))
