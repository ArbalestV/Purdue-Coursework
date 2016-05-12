(define (greater-than m n)
 (cond ((zero? m) #f)
       ((zero? n) #t)
       (else (greater-than (- m 1) (- n 1)))))

(define (sort l)
 (cond
  ((= (length l) 0)
   l)
  ((= (length l) 1)
   l)
  ((= (length l) 2)
   (case (greater-than (first l) (second l))
    ((#f) l)
    ((#t) (append (list (second l)) (list (first l))))))
  ;;inductive case
  (else
   (let ((rest-sorted (sort (rest l))))
    ;;(display rest-sorted)
    ;;(display newline)
    (case (greater-than (first l) (first rest-sorted))
     ((#f) (append (list (first l)) rest-sorted))
     ((#t) (append (list (first rest-sorted))
		   (sort (append (list (first l)) (rest rest-sorted))))))))))

(define (remove-all x l)
 (cond ((null? l) (list))
       ((equal? (first l) x) (remove-all x (rest l)))
       (else (cons (first l) (remove-all x (rest l))))))

;; (define (remove-one x list)
;;  (cond ((null? list) (list))
;;        ((equal? (first list) x) (rest list))
;;        (else (cons (first list) (remove-one x (rest list))))))
  

;; (define (all-permutations l)
;;  (if (null? l) (list)
;;      (apply append
;; 	    (map (lambda (element)
;; 		  (map (lambda (permutation)
;; 			(cons element permutation))
;; 		       (all-permutations (remove-all element l))))
;; 		 l))))
				