;; n++
;; 2++
;; pi++
;; my_bank_account += 10000000000000000000000000000000000000000000000000000
(define (increment n) (+ n 1))

(define (decrement n) (- n 1))

(define zero 0)

(define (is-zero? n) (zero? n))

;;(define (increment n) (cons 'rock n))

;;(define (decrement n) (rest n))

;;(define zero '())

;;(define (is-zero? n) (null? n))

(define (plus m n)
 (if (is-zero? n)
     m
     (plus (increment m) (decrement n))))

(define (minus m n)
 (if (is-zero? n)
     m
     (minus (decrement m) (decrement n))))

(define (times m n)
 (if (is-zero? n)
     zero
     (plus m (times m (decrement n)))))

(define (divide m n)
 (if (is-zero? m)
     zero
     (increment (divide (minus m n) n))))
