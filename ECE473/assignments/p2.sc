;;;all previous code
(define (memberof B A)
 (cond ((null? A) #f)
       ((equal? B (first A)) #t)
	(else (memberof B (rest A)))))

(define (set-union A B)
 (cond ((null? B) (remove-duplicates A))
       ((null? A) (remove-duplicates B))
       (else (if (memberof (first B) A)
		 (remove-duplicates (set-union A (rest B)))
		 (remove-duplicates (set-union (cons (first B) A) (rest B)))))))
	    
(define (set-minus A B)
 (cond ((null? A) '())
       ((null? B) (remove-duplicates A))
       (else (if (memberof (first A) B)
		 (remove-duplicates (set-minus (rest A) B))
		 (remove-duplicates (cons (first A) (set-minus (rest A) B)))))))
	    
(define (set-intersection A B)
 (cond ((null? A) '())
       ((null? B) '())
       (else (if (memberof (first A) B)
		 (remove-duplicates (cons (first A) (set-intersection (rest A) B)))
		 (remove-duplicates (set-intersection (rest A) B))))))
	  

(define (factorial n)
 (if (= n 0)
     1
     (* n (factorial (- n 1)))))


(define (distance x1 y1 x2 y2)
 (sqrt (+ (sqr (- x2 x1)) (sqr (- y2 y1)))))

(define (increment n) (+ n 1))
(define (decrement n) (- n 1))

(define (plus m n)
 (if (zero? n)
     m
     (increment (plus m (decrement n)))))

(define (minus m n)
 (if (zero? n)
     m
     (decrement (minus m (decrement n)))))

(define (multiply m n)
 (if (zero? n)
     0
     (plus (multiply m (decrement n)) m)))

(define (divide m n)
 (if (zero? m)
     0
     (increment (divide (minus m n) n))))


;; (define (less-than m n)
;;  (if (zero? n)
;;      #f
;;      (if (zero? m)
;; 	 #t
;; 	 (less-than (decrement m) (decrement n)))))

(define (less-than m n)
 (cond ((zero? n) #f)
       ((zero? m) #t)
       (else (less-than (decrement m) (decrement n)))))

(define (length list)
 (if (null? list)
     0
     (+ (length (rest list)) 1)))

(define (list-ref list i)
 (if (= i 0)
     (first list)
     (list-ref (rest list) (- i 1))))

(define (list-replace-ith list i x)
 (if (= i 0)
     (cons x (rest list))
     (cons (first list)
	   (list-replace-ith (rest list) (decrement i) x))))

(define (list-insert-ith list i x)
 (if (= i 0)
     (cons x list)
     (cons (first list)
	   (list-insert-ith (rest list) (decrement i) x))))

(define (list-remove-ith list i)
 (if (= i 0)
     (rest list)
     (cons (first list)
	   (list-remove-ith (rest list) (decrement i)))))

(define (member? x list)
 (cond ((null? list) #f)
       ((= x (first list)) #t)
       (else (member? x (rest list)))))

(define (position x list)
 (cond ((null? list) (panic "Element not found"))
       ((= (first list) x) 0)
       (else (+ (position x (rest list)) 1))))

(define (remove-one x list)
 (cond ((null? list) (list))
       ((= (first list) x) (rest list))
       (else (cons (first list) (remove-one x (rest list))))))

(define (remove-all x list1)
 (cond ((null? list1) (list))
       ((equal? (first list1) x) (remove-all x (rest list1)))
       (else (cons (first list1) (remove-all x (rest list1)))))) 

(define (replace-one x y list)
 (cond ((null? list) (list))
       ((equal? (first list) x) (cons y (rest list)))
       (else (cons (first list) (replace-one x y (rest list))))))

(define (replace-all x y list1)
 (cond
  ((null? list1) (list))
  ((equal? (first list1) x) (cons y (replace-all x y (rest list1))))
  (else (cons (first list1) (replace-all x y (rest list1)))))) ;;again not working

(define (append list1 list2)
 (if (null? list1)
     list2
     (cons (first list1) (append (rest list1) list2))))

(define (reverse l)
 (if (null? l)
     (list)
     (append (reverse (rest l)) (list (first l)))))

(define (sum list)
 (if (null? list)
     0
     (+ (first list) (sum (rest list)))))

(define (product list)
 (if (null? list)
     1
     (* (first list) (product (rest list)))))

(define (eqv? x y)
 (or (and (boolean? x) (boolean? y)
	  (eq? x y))
     (and (number? x) (number? y)
	  (= x y))
     (and (symbol? x) (symbol? y)
	  (eq? x y))
     (and (char? x) (char? y)
	  (char=? x y))
     (and (string? x) (string? y)
	  (string=? x y))
     (and (null? x) (null? y))))

(define (equal? x y)
 (or (eqv? x y)
     (and (list? x)
	  (list? y)
	  (not (null? x))
	  (not (null? y))
	  (equal? (first x) (first y))
	  (equal? (rest x) (rest y)))))

(define (map procedure list)
 (if (null? list)
     '()
     (cons (procedure (first list))
	   (map procedure (rest list)))))

(define (list-sum list)
 (if (null? list)
     0
     (+ (first list) (list-sum (rest list)))))

(define (list-product list)
 (if (null? list)
     1
     (* (first list) (list-product (rest list)))))

(define (reduce procedure list identity)
 (if (null? list)
     identity
     (procedure (first list)
		(reduce procedure (rest list) identity))))

(define (list-sum list) (reduce + list 0))
(define (list-product list) (reduce * list 1))

(define (map-reduce g f l i) (reduce g (map f l) i))

;;end of all previous code

;; (define (calculate e)
;;  (cond
;;   ((number? e) e)
;;   ((list? e)
;;    (if (null? e)
;;        (panic "invalid expression")
;;        (case (first e)
;; 	((+) (map-reduce + 0 calculate (rest e)))
;; 	((-) (case (length (rest e))
;; 	      ((0) (panic "- must take one or more arguments"))
;; 	      ((1) (- (calculate (second e))))
;; 	      (else (+ (calculate (second e))
;; 		       (- (map-reduce + 0 calculate (rest (rest e))))))))
;; 	((*) (map-reduce * 1 calculate (rest e)))
;; 	((/) (case (length (rest e))
;; 	      ((0) (panic "/ must take one or more arguments"))
;; 	      ((1) (/ (calculate (second e))))
;; 	      (else (* (calculate (second e))
;; 		       (/ (map-reduce * 1 calculate (rest (rest e))))))))
;; 	((sqrt) (if (= (length (rest e)) 1)
;; 		    (sqrt (calculate (second e)))
;; 		    (panic "sqrt must take exactly one argument")))
;; 	((expt) (if (= (length (rest e)) 2)
;; 		    (expt (calculate (second e)) (calculate (third e)))
;; 		    (panic "expt must take exactly two arguments")))
;; 	(else (panic "invalid operator")))))
;;   (else (panic "invalid expression"))))


;;; (compute expression environment) ===> value

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
;;; - (if e1 e2 e3), where e1, e2, and e3 are expressions, or
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
	(else (let* ((function-name (first e))
		     (definition (lookup-definition function-name definitions))
		     (values (map compute-with-environment (rest e)))
		     (variables (rest (second definition)))
		     (environment (make-environment variables values))
		     (body (third definition)))
	       (compute body environment definitions))))))
  (else (panic "invalid expression"))))


;;;;;beginning of code for problem set 2
;;start with getting the list of propositions that a formula might contain
(define (get-propositions formula)
 (cond
  ((null? formula) (list)) ;;taken care of empty formula, just return the empty list suggesting no propositions
  ((boolean? formula) 
   (list)) ;;if only booleans, then no propositions, hence return the empty list
  ((symbol? formula)
   (list formula)) ;;if the formula is a symbol, i.e, a proposition, then return the proposition in a list
  ((= (length formula) 1)
   (get-propositions (first formula))) ;;if the formula contains a list of length one, then recurse on one of the base conditions
  ((equal? (first formula) 'not)
   (get-propositions (rest formula))) ;;if it begins with a not, then it will have the same propositions as the rest of the formula
  ;;if it didn't meet any of the conditions above, then it must be an and/or operation. In that case, the main recursion step is called -> set-minus is called with (and or) so as to remove and/or from the list if there is no parentheses around any of the 'and'/'or' operations
  (else (set-minus (set-union (get-propositions (second formula)) (get-propositions (rest formula))) '(and or not)))))
;;;get-propositions tested fairly thoroughly. Works as expected.

;;now, define what a binding is wrt to the propositions that a formula might contain. Here, we will define generically what a binding is for a proposition within the setting of a propositional/boolean logic.

;;let us define what a binding is for our propositional logic.
(define (is-a-binding probable-binding) ;;a function to check whether it is a binding or not; we are first going to check if the passed argument is a list. If it is not, then return false. Otherwise, we will check if the first element is a symbol and the second is a boolean. Unless both conditions are satisfied, return false.
 (cond
  ((not (list? probable-binding))
   #f);; if it is not a list, then immediately return false
  ((not (equal? (length probable-binding) 2))
   #f) ;;basically it has to be a list of exactly 2 items, since we are looking for a binding. If the length is not 2, then it cannot be a binding
  (else
   (and (symbol? (first probable-binding)) (boolean? (second probable-binding))))))
;;;is-a-binding tested fairly thoroughly. Works as expected.

;;now, let us define a truth assignment is. Essentially, it will be similar to its binding counterpart, except scaled/extended to include the given definition of a truth assignment which is essentially a list of bindings.
(define (is-a-truth-assignment probable-truth-assignment) ;;check if the passed argument is a list or no. If no, then return false. If yes, then check recursively if each element for a binding or not, and they all have to be anded together. This will in turn check for things like lengths of individual items within a probable truth assignment,etc.
 (cond
  ((and (list? probable-truth-assignment) (= (length probable-truth-assignment) 0))
   #t) ;;new condition added on saturday
  ((not (list? probable-truth-assignment))
   #f) ;;if it is not a list, then immediately return false
  ((= (length probable-truth-assignment) 1) ;;if the length of the list is 1, then just check whether that element is a binding or not
   (is-a-binding (first probable-truth-assignment)))
  ((= (length probable-truth-assignment) 2) ;;if the length of the list is 2, then just check whether the two elements are both bindings or not
   (and (is-a-binding (first probable-truth-assignment)) (is-a-binding (second probable-truth-assignment))))
  (else
   (and (is-a-binding (first probable-truth-assignment)) (is-a-truth-assignment (rest probable-truth-assignment))))))
;;;is-a-truth-assignment tested fairly thoroughly. Works as expected.

;;;now start off by getting all the possible bindings from a given formula. For this you will have get the list of propositions.

(define (make-a-binding symb bool-val) ;;a function to make a binding p->#f or p->#t
 (cond
  ((not (and (symbol? symb) (boolean? bool-val))) ;;if not a symbol or not a boolean value
   (panic "Binding must be between a symbol and a boolean."))
  (else
   (list symb bool-val) ;;make the binding and return it
   )))
;;checked extensively - works fine

(define (make-all-possible-bindings symb) ;;function to make all the possible bindings for a given symbol
 (cond
  ((not (symbol? symb))
   (panic "Binding has start with a symbol."))
  (else
   (list (make-a-binding symb #t) (make-a-binding symb #f))))) ;;make the list of all possible bindings for a particular symbol
;;checked - works fine.

(define (bindings-for-propositions list-prop) ;;make a list of all propositions for a list of propositions
 (cond
  ((not (list? list-prop)) ;;the given list is not a list
   (panic "Must have a list."))
  (else
   (if (= (length list-prop) 0)
       (list) ;;return the empty list is empty, otherwise there will be an issue with set-union since there will be no pair present for the terminal condition
       (set-union (make-all-possible-bindings (first list-prop)) (bindings-for-propositions (rest list-prop)))))))
;;;tested - works.

(define (all-bindings-for-formula formula) ;;function to extract the propositions from a formula, and then make a list of all the possible bindings
 ;;first of all, we have to get the list of propositions, then check if the list is not empty. If empty, then return an empty list. If it is not empty, then we will take one proposition at a time and make a union of all bindings.
 (let ((list-prop (get-propositions formula)))
  (if (= (length list-prop) 0)
      (list) ;;if the list of propositions is empty, then no bindings. Return the empty list.
      (bindings-for-propositions list-prop)))) ;;otherwise call the function to get all possible bindings for list of propositions.
;;tested - works


;;;work on defining different types of truth assignments. - Day3
(define (consistent-truth-assignment truth-assignment prop-list) ;;define what the definition of a consistent binding is. Prop-list will initially be empty list.
 ;;first of check if the given binding is a list, or that it is an actual truth assignment
 (cond
  ((not (list? truth-assignment))
   (panic "Truth Assignment must be a list."))
  ((not (is-a-truth-assignment truth-assignment))
   (panic "Given list not a truth assignment."))
  (else ;;idea is to keep inserting new propositions into this list. The moment wee see that a proposition already exists, then that would mean that the truth assignment is inconsistent.
   (cond
    ((memberof (first (first truth-assignment)) prop-list) ;;if the proposition from a particular binding is already existing in the symbol list, then return false
     #f)
    (else
     (cond
      ((= (length (rest truth-assignment)) 0)
       #t)
      (else	
       (consistent-truth-assignment (rest truth-assignment) (set-union prop-list (list (first (first truth-assignment))))))))))))
;;;tested - works

(define (propositions-in-assignment truth-assignment)
 (cond
  ((not (is-a-truth-assignment truth-assignment))
   (panic "Given list not a truth assignment."))
  (else
   (cond
    ((= (length truth-assignment) 0)
     (list))
    (else
     (set-union (list (first (first truth-assignment))) (propositions-in-assignment (rest truth-assignment))))))))
;;tested - works

(define (complete-truth-assignment truth-assignment formula)
 (cond
  ((not (list? truth-assignment))
   (panic "Truth Assignment must be a list."))
  ((not (is-a-truth-assignment truth-assignment))
   (panic "Given list not a truth assignment."))
  ((boolean? formula)
   #t)
  (else
   (let ((prop-formula (get-propositions formula))
	 (prop-assignment (propositions-in-assignment truth-assignment)))
    ;; (and (equal? (set-minus prop-formula prop-assignment) '()) (equal? (set-minus prop-assignment prop-formula) '()))
    (equal? (set-minus prop-formula prop-assignment) '())))))
;;tested - works

(define (redundant-truth-assignment truth-assignment formula)
 (let ((prop-formula (get-propositions formula))
       (prop-assignment (propositions-in-assignment truth-assignment)))
  (not (equal? (set-minus prop-assignment prop-formula) '()))))

(define (nonredundant-truth-assignment truth-assignment formula)
 (not (redundant-truth-assignment truth-assignment formula)))

;;both above functions tested - work fine

(define (complete-consistent-truth-assignment truth-assignment formula)
 ;;(= (length truth-assignment) 0)
 (and (consistent-truth-assignment truth-assignment '()) (complete-truth-assignment truth-assignment formula)))
;;tested - works.

(define (lookup-assignment proposition assignment-list)
 (cond
  ((null? assignment-list)
   (panic "Unassigned proposition."))
  ((eq? (first (first assignment-list)) proposition)
   (second (first assignment-list)))
  (else
   (lookup-assignment proposition (rest assignment-list)))))

(define (valuation-function truth-assignment formula)
 ;;(display (complete-truth-assignment truth-assignment formula))
 ;;(newline)
 ;;(display (consistent-truth-assignment truth-assignment '()))
 ;;(newline)
 (cond
  ((not (complete-consistent-truth-assignment truth-assignment formula))
   (panic "The given truth assignment should be consistent and complete for the given formula."));;if not complre consistent, then just display error.
  ((boolean? formula)
   formula)
  ((symbol? formula)
   (lookup-assignment formula truth-assignment))
  ((= (length formula) 1)
   (valuation-function truth-assignment (first formula)))
  ((equal? (first formula) 'not)
   (not (valuation-function truth-assignment (rest formula))))
  ((equal? (first formula) 'and)
   (and (valuation-function truth-assignment (second formula)) (valuation-function truth-assignment (rest (rest formula)))))
  ((equal? (first formula) 'or)
   (or (valuation-function truth-assignment (second formula)) (valuation-function truth-assignment (rest (rest formula)))))))
;;tested - works as expected. Checked with multiple examples of varying types.

(define (complete-consistent-nonredundant truth-assignment formula)
 (and (complete-consistent-truth-assignment truth-assignment formula)
      (nonredundant-truth-assignment truth-assignment formula)))
;;tested - works as expected

(define (row truth-assignment formula)
 (cond
  ((= (length truth-assignment) 0)
   (list))
  ((not (complete-consistent-nonredundant truth-assignment formula))
   (panic "The truth assignment is not complete, consistent, nonredundant wrt the given formula."))
  (else
   (list truth-assignment (valuation-function truth-assignment formula)))))
;;tested - works as expected

(define (total-rows formula)
 (expt 2 (length (get-propositions formula)))) 
;;tested - works as expected

(define (append-a-binding binding truth-assignment)
 (cond
  ((= (length truth-assignment) 0)
   (list))
  (else
   ;; (set-union (list (append (list binding) (list (first truth-assignment)))) (append-a-binding binding (rest truth-assignment)))
   (list (append (list binding) truth-assignment)))))

(define (append-all-bindings all-possible-bindings truth-assignment)
 (set-union (append-a-binding (first all-possible-bindings) truth-assignment) (append-a-binding (second all-possible-bindings) truth-assignment)))

(define (append-bindings-for-proposition proposition truth-assignment)
 (let ((all-possible-bindings (make-all-possible-bindings proposition)))
  (append-all-bindings all-possible-bindings truth-assignment)))

(define (append-bindings-proposition-assignments proposition truth-assignment-list)
 (cond
  ((= (length truth-assignment-list) 0)
   (list))
  (else
   (set-union (append-bindings-for-proposition proposition (first truth-assignment-list)) (append-bindings-proposition-assignments proposition (rest truth-assignment-list))))))

(define (make-all-rows prop-list)
 ;;(let ((prop-list (get-propositions formula)))
 (cond
  ((= (length prop-list) 0)
   (list))
  ((= (length prop-list) 1)
   (set-union (list (list (make-a-binding (first prop-list) #f))) (list (list (make-a-binding (first prop-list) #t)))))
  (else
   ;; (display "in progress...")
   ;; (append-bindings-proposition-assignments (second prop-list) (make-all-rows (list (first prop-list))))
   (append-bindings-proposition-assignments (first prop-list) (make-all-rows (rest prop-list))))))

(define (valuation-for-rows row-list formula)
 (cond
  ((= (length row-list) 0)
   (list))
  (else
   (set-union (list (row (first row-list) formula)) (valuation-for-rows (rest row-list) formula)))))

(define (truth-table formula)
;; (let ((prop-list (get-propositions formula)))
;;  (display prop-list)
;;  (newline)
;;  (let ((all-rows (make-all-rows prop-list)))
;;   (display all-rows)
;;   (valuation-for-rows all-rows prop-list)))
 (valuation-for-rows (make-all-rows (get-propositions formula)) formula))


;;;assignment code for problem set 3

(define (checking-rows? rows_all formula1 formula2)
 (and (equal? (row (first rows_all) formula1) (row (first rows_all) formula2)) (checking-rows? rows_all (rest formula1) (rest formula2))))

(define (check-if-rows-equal? formula1 formula2)
 (let ((rows_all (make-all-rows (get-propositions formula1))))
  (checking-rows? rows_all formula1 formula2)))
   
(define (truth-tables-match? formula1 formula2)
 (cond
   ;; ((not (equal? (length tt1) (length tt2)))
   ;;  #f)
   ((not (null? (set-minus (get-propositions formula1) (get-propositions formula2))))
    (display "not equal.")
    #f)
   (else
    (display "checking for rows.")
    (check-if-rows-equal? formula1 formula2)))
 ;; (let ((tt1 (truth-table formula1))
 ;;       (tt2 (truth-table formula2)))
 ;;  ;; (sets-equal tt1 tt2)
 ;;  (cond
 ;;   ((not (equal? (length tt1) (length tt2)))
 ;;    #f)
 ;;   ((not (equal? (get-propositions formula1) (get-propositions formula2)))
 ;;    #f)
 ;;   (else
 ;;    (check-if-rows-equal? formula1 formula2))))
 )
  

  
  

      

  




	
	