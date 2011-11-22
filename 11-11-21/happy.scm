; 4 is part of the crazy unhappy loop of life
(define (badseq? n)
    (= n 4)
)

(define (happy? n)
    (if (= n 0)
        #f
        (if (= n 1) ; 1 is happy
            #t 
            (if (badseq? n) ; is in the unhappy numbers
                #f 
                (happy? (happy-transform n))
            )
        )
    )
)

(define (happy-transform n)
    (if (= n 0)
        n
        (+ 
            (sqr (modulo n 10)) 
            (happy-transform (quotient n 10))
        )
    )
)

