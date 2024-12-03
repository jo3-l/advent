#lang racket

(provide solve)

(require test-engine/racket-tests)

(define (solve xs ys)
  (distance (sort xs <) (sort ys <)))
(define (solve/fp xs ys)
  (distance/fp (sort xs <) (sort ys <)))

;; distance: (listof Int) (listof Int) -> Int
(define (distance xs ys)
  (cond
    [(empty? xs) 0]
    [else (+ (abs (- (first xs) (first ys))) (distance (rest xs) (rest ys)))]))

(define (distance/fp xs ys)
  (foldr (lambda (x y acc) (+ (abs (- x y)) acc)) 0 xs ys))

(define xs '(3 4 2 1 3 3))
(define ys '(4 3 5 3 9 3))
(check-expect (solve xs ys) 11)
(check-expect (solve/fp xs ys) 11)
