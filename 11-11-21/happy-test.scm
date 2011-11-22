(require rackunit)
(require rackunit/text-ui)

(include "happy.scm")

(define-test-suite happy-test
    (check-true (happy? 1) "1 is happy")
    (check-true (happy? 10) "10 is happy")
    (check-false (happy? 2) "2 ain't happy :(")
    (check-false (happy? 3) "3 ain't happy :(")
    (check-false (happy? 0) "what's really 0?")
    (check-true (happy? 7) "seven is happy?")
    (check-false (happy? 6) "six is happy?")
)

(run-tests happy-test 'normal)
