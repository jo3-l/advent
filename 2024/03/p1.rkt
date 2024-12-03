#lang racket

(provide solve)

(require test-engine/racket-tests)

(define (solve prog)
  (define products
    (map (lambda (m)
           (define x (string->number (first m)))
           (define y (string->number (second m)))
           (* x y))
         (regexp-match* #px"mul\\((\\d{1,3}),(\\d{1,3})\\)" prog #:match-select rest)))
  (foldr + 0 products))

(check-expect (solve "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))") 161)
