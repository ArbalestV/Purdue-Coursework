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
	    
	    

	 
	
	
       
       
	    
	    
       
	    
       