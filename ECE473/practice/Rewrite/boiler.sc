;;; instruction (load r x)
;;;             (store r x)
;;;             null?
;;;             first
;;;             rest
;;;             cons
;;;             (jump l)
;;;             (jump-if-false l)

;;; ROM-contents is
;;; ([pc] (ROM-address1 instruction1) [pc] (ROM-address2 instruction2) [pc] ...)
;;; RAM-contents is
;;; ((a v) (b v) (0 v) ... (15 v))
;;; machine state is (ROM-contents RAM-contents)

;;; i is an instructions
;;; j is a (ROM-address instruction)
;;; k is a RAM-address
;;; l is a ROM-address
;;; m is a (RAM-address/register value)
;;; r is a register
;;; v is a value
;;; x is a RAM-address

;;; machine state -~-> machine state

(define *boilerchip*
 '(;; (load r x)
   (((j1... pc (l1 (load r x)) j2...) (m1... (r v1) m2... (x v2) m3...))
    -~->
    ((j1... (l1 (load r x)) pc j2...) (m1... (r v2) m2... (x v2) m3...)))
   ;; (store r x)
   (((j1... pc (l1 (store r x)) j2...) (m1... (r v1) m2... (x v2) m3...))
    -~->
    ((j1... (l1 (store r x)) pc j2...) (m1... (r v1) m2... (x v1) m3...)))
   ;; null?
   (((j1... pc (l1 null?) j2...) ((a ()) m...))
    -~->
    ((j1... (l1 null?) pc j2...) ((a #t) m...)))
   (((j1... pc (l1 null?) j2...) ((a (v v...)) m...))
    -~->
    ((j1... (l1 null?) pc j2...) ((a #f) m...)))
   ;; first
   (((j1... pc (l1 first) j2...) ((a (v v...)) m...))
    -~->
    ((j1... (l1 first) pc j2...) ((a v) m...)))
   ;; rest
   (((j1... pc (l1 rest) j2...) ((a (v v...)) m...))
    -~->
    ((j1... (l1 rest) pc j2...) ((a (v...)) m...)))
   ;; cons
   (((j1... pc (l1 cons) j2...) ((a v) (b (v...)) m...))
    -~->
    ((j1... (l1 cons) pc j2...) ((a (v v...)) (b (v...)) m...)))
   ;; (jump l)
   (((j1... pc (l1 (jump l)) j2... (l i) j3...) k)
    -~->
    ((j1... (l1 (jump l)) j2... pc (l i) j3...) k))
   (((j1... (l i) j2... pc (l1 (jump l)) j3...) k)
    -~->
    ((j1... pc (l i) j2... (l1 (jump l)) j3...) k))
   ;; (jump-if-false l)
   (((j1... pc (l1 (jump-if-false l)) j2... (l i) j3...) ((a #f) m...))
    -~->
    ((j1... (l1 (jump-if-false l)) j2... pc (l i) j3...) ((a #f) m...)))
   (((j1... (l i) j2... pc (l1 (jump-if-false l)) j3...) ((a #f) m...))
    -~->
    ((j1... pc (l i) j2... (l1 (jump-if-false l)) j3...) ((a #f) m...)))
   (((j1... pc (l1 (jump-if-false l)) j2...) ((a #t) m...))
    -~->
    ((j1... (l1 (jump-if-false l)) pc j2...) ((a #t) m...)))))

(define (expression-variable? pattern)
 (member pattern '(i k l l1 l2 m r v v1 v2 x)))

(define (expression-sequence-variable? pattern)
 (member pattern '(j1... j2... j3... m... m1... m2... m3... v...)))

(define (plus x y) (if (null? x) y (plus (rest x) (cons #t y))))

(define *plus-ROM*
 ;; // 0 must be initialized to #t
 ;;     store a 1
 ;;     store b 2
 ;; l1: load a 1
 ;;     null?
 ;;     jump-if-false l2
 ;;     jump l3
 ;; l2: load a 1
 ;;     rest
 ;;     store a 1
 ;;     load a 0
 ;;     load b 2
 ;;     cons
 ;;     store a 2
 ;;     jump l1
 ;; l3: load a 2
 '((n0 (store a 1))
   (n1 (store b 2))
   (n2 (load a 1))
   (n3 null?)
   (n4 (jump-if-false n6))
   (n5 (jump n14))
   (n6 (load a 1))
   (n7 rest)
   (n8 (store a 1))
   (n9 (load a 0))
   (n10 (load b 2))
   (n11 cons)
   (n12 (store a 2))
   (n13 (jump n2))
   (n14 (load a 2))))

(define (peano-plus x y)
 (length (plus (map (lambda (i) #t) (enumerate x))
	       (map (lambda (i) #t) (enumerate y)))))

(define (initial-state x y)
 (list (cons 'pc *plus-ROM*)
       (list (list 'a x)
	     (list 'b y)
	     (list 0 #t)
	     (list 1 #f)
	     (list 2 #f))))

(define (boiler-plus x y)
 (length
  (second
   (first
    (second
     (rewrite (initial-state (map (lambda (i) #t) (enumerate x))
			     (map (lambda (i) #t) (enumerate y)))
	      *boilerchip*))))))
