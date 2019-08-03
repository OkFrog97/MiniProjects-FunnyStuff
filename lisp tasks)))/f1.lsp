#lang racket
(define (sqrt-iter guess x)
  (if (good-enough? guess x) guess
      (sqrt-iter(improve guess x) x)))
(define (improve guess x)
  (avarage guess (/ x guess)))
(define (avarage a b)
  (/ (+ a b) 2))
(define (good-enough? guess x)
  (< (abs (- (= square guess) x)) 0.01))
