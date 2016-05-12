(define (length l)
 (if (null? l)
     zero
     (increment (length (rest l)))))

(define (list-ref l i)
 (if (is-zero? i)
     (first l)
     (list-ref (rest l) (decrement i))))

;; l[i]=x
(define (list-replace-ith l i x)
 (if (is-zero? i)
     (cons x (rest l))
     (cons (first l) (list-replace-ith (rest l) (decrement i) x))))

(define (list-insert-ith l i x)
 (if (is-zero? i)
     (cons x l)
     (cons (first l) (list-insert-ith (rest l) (decrement i) x))))

(define (list-remove-ith l i)
 (if (is-zero? i)
     (rest l)
     (cons (first l) (list-remove-ith (rest l) (decrement i)))))

(define (member? x l)
 (cond ((null? l) #f)
       ((= x (first l)) #t)
       (else (member? x (rest l)))))

(define (position x l)
 (cond ((null? l) #f)
       ((= (first l) x) zero)
       (else (let ((result (position x (rest l))))
	      (if (boolean? result)
		  result
		  (increment result))))))

(define (remove-one x l)
 (if (member? x l)
     (list-remove-ith l (position x l))
     l))

(define (remove-all x l)
 (if (member? x l)
     (remove-all x (remove-one x l))
     l))

(define (remove-one x l)
 (cond ((null? l) l)
       ((= x (first l)) (rest l))
       (else (cons (first l) (remove-one x (rest l))))))

(define (remove-all x l)
 (cond ((null? l) l)
       ((= x (first l)) (remove-all x (rest l)))
       (else (cons (first l) (remove-all x (rest l))))))

(define (replace-one x y l)
 (if (member? x l)
     (list-replace-ith l (position x l) y)
     l))

(define (replace-all x y l)
 (if (member? x l)
     (replace-all x y (replace-one x y l))
     l))

(define (replace-one x y l)
 (cond ((null? l) l)
       ((= x (first l)) (cons y (rest l)))
       (else (cons (first l) (replace-one x y (rest l))))))

(define (replace-all x y l)
 (cond ((null? l) l)
       ((= x (first l)) (cons y (replace-all x y (rest l))))
       (else (cons (first l) (replace-all x y (rest l))))))

;; (append (list 1 2) (list 3 4))
;; =(cons (first (list 1 2)) (append (rest (list 1 2)) (list 3 4)))
;; =(cons 1 (append (rest (list 1 2)) (list 3 4)))
;; =(cons 1 (append (list 2) (list 3 4)))
;; =(cons 1 (cons (first (list 2)) (append (rest (list 2)) (list 3 4))))
;; =(cons 1 (cons 2 (append (rest (list 2)) (list 3 4))))
;; =(cons 1 (cons 2 (append (list) (list 3 4))))
;; =(cons 1 (cons 2 (list 3 4)))
;; =(cons 1 (list 2 3 4))
;; =(list 1 2 3 4)

(define (append l1 l2)
 (if (null? l1)
     l2
     (cons (first l1) (append (rest l1) l2))))

(define (reverse l)
 (if (null? l)
     l
     (append (reverse (rest l)) (list (first l)))))

(define (reduce g l i)
 (if (null? l)
     i
     (g (first l) (reduce g (rest l) i))))

(define (map f l)
 (if (null? l)
     l
     (cons (f (first l)) (map f (rest l)))))

(define (map-reduce g f l i) (reduce g (map f l) i))

(define (google) (map-reduce max page-rank *the-world-wide-web* minus-infinity))
