#lang racket

(define-struct eqn (target inputs))

(define (solve/part1 eqns)
  (sum-satisfiable-targets eqns (list + *)))
(define (solve/part2 eqns)
  (define (concat a b)
    (string->number (string-append (number->string a) (number->string b))))
  (sum-satisfiable-targets eqns (list + * concat)))

(define (sum-satisfiable-targets eqns ops)
  (define good-eqs (filter (lambda (eqn) (satisfiable? eqn ops)) eqns))
  (foldl (lambda (eqn acc) (+ (eqn-target eqn) acc)) 0 good-eqs))

(define (satisfiable? eqn ops)
  (define (go target acc inputs)
    (cond
      [(empty? inputs) (= acc target)]
      [else (ormap (lambda (op) (go target (op acc (first inputs)) (rest inputs))) ops)]))

  (define inputs (eqn-inputs eqn))
  (go (eqn-target eqn) (first inputs) (rest inputs)))

(define (parse-input)
  (define (line->eqn line)
    (define parts (string-split line ": "))
    (define inputs (map string->number (string-split (second parts))))
    (make-eqn (string->number (first parts)) inputs))

  (map line->eqn (file->lines "input.txt")))

(define eqns (parse-input))
(printf "part 1: ~a\n" (solve/part1 eqns))
(printf "part 2: ~a\n" (solve/part2 eqns))
