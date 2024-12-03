#lang racket

(provide solve
         solve/hashed)

(require test-engine/racket-tests)

(define (solve xs ys)
  (foldr (lambda (x acc) (+ acc (* x (count-appearances ys x)))) 0 xs))
(define (count-appearances xs x)
  (foldr (lambda (y acc) (if (= y x) (add1 acc) acc)) 0 xs))

(define (solve/hashed xs ys)
  (define y-freqs (make-hash))
  (set-freqs! y-freqs ys)
  (foldr (lambda (x acc) (+ acc (* x (lookup-freq y-freqs x)))) 0 xs))
(define (set-freqs! ht xs)
  (when (not (empty? xs))
    (define k (first xs))
    (hash-set! ht k (add1 (lookup-freq ht k)))
    (set-freqs! ht (rest xs))))
(define (lookup-freq ht k)
  (hash-ref ht k 0))

(define xs '(3 4 2 1 3 3))
(define ys '(4 3 5 3 9 3))
(check-expect (solve xs ys) 31)
(check-expect (solve/hashed xs ys) 31)
