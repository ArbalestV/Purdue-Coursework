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

(define (remove-all x list)
 (cond ((null? list) (list))
       ((= (first list) x) (remove-all x (rest list)))
       (else (cons (first list) (remove-all x (rest list)))))) ;;;=> not working somehow

(define (replace-one x y list)
 (cond ((null? list) (list))
       ((= (first list) x) (cons y (rest list)))
       (else (cons (first list) (replace-one x y (rest list))))))

(define (replace-all x y list)
 (cond
  ((null? list) (list))
  ((= (first list) x) (cons y (replace-all x y (rest list))))
  (else (cons (first list) (replace-all x y (rest list)))))) ;;again not working

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

;;first calculator definition

(define (calculate expression)
 (cond ((number? expression) expression)
       ((list? expression)
	(case (first expression)
	 ((+) (calculate-+ (rest expression)))
	 ((-) (calculate-- (rest expression)))
	 ((*) (calculate-* (rest expression)))
	 ((/) (calculate-/ (rest expression)))
	 ((expt) (calculate-expt (rest expression)))
	 ((sqrt) (calculate-sqrt (rest expression)))))))

(define (calculate-+ arguments)
 (reduce + (map calculate arguments) 0))

(define (calculate-- arguments)
 (if (= (length arguments) 1)
     (- (calculate (first arguments)))
     (- (calculate (first arguments))
	(reduce + (map calculate (rest arguments)) 0))))

(define (calculate-* arguments)
 (reduce * (map calculate arguments) 1))

(define (calculate-/ arguments)
 (if (= (length arguments) 1)
     (/ (calculate (first arguments)))
     (/ (calculate (first arguments))
	(reduce * (map calculate (rest arguments)) 1))))

(define (calculate-expt arguments)
 (expt (calculate (first arguments))
       (calculate (second arguments))))

(define (calculate-sqrt arguments)
 (sqrt (calculate (first arguments))))


;;;;;;second calculator definition -> more understandable. This is the one coded up in class.

(define (calculate2 e)
 (cond ((number? e) e)
       ((and (list? e) (not (null? e)))
	(case (first e)
	 ((+) (calculate2-+ (map calculate (rest e))))
	 ((-) (calculate2-- (map calculate (rest e))))
	 ((*) (calculate2-* (map calculate (rest e))))
	 ((/) (calculate2-/ (map calculate (rest e))))
	 ((expt) (calculate2-expt (map calculate (rest e))))
	 ((sqrt) (calculate2-sqrt (map calculate (rest e))))
	 (else (panic "Invalid expression"))))
       (else (panic "Invalid expression"))))

(define (calculate2-+ arguments) (reduce + arguments 0))

(define (calculate2-- arguments)
 (cond ((null? arguments) (panic "- cannot take zero arguments"))
       ((= (length arguments) 1) (- (first arguments)))
       (else (- (first arguments) (reduce + (rest arguments) 0)))))

(define (calculate2-* arguments) (reduce * arguments 1))

(define (calculate2-/ arguments)
 (cond ((null? arguments) (panic "/ cannot take zero arguments"))
       ((= (length arguments) 1) (/ (first arguments)))
       (else (/ (first arguments) (reduce * (rest arguments) 1)))))

(define (calculate2-expt arguments)
 (if (= (length arguments) 2)
     (expt (first arguments) (second arguments))
     (panic "EXPT must take exactly two arguments.")))

(define (calculate2-sqrt arguments)
 (if (= (length arguments) 1)
     (sqrt (first arguments))
     (panic "SQRT must take exactly one argument.")))


