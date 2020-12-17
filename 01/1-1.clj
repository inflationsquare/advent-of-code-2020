(require '[clojure.java.io :as io])
(require '[clojure.edn :as edn])

(let [data (with-open [rdr (io/reader "1-1.in")] (doall (map edn/read-string (line-seq rdr))))]
(println 
  (reduce * 
    (first 
       (filter 
    (fn [x] (= (reduce + x) 2020)) (for [x data y data] (vector x y)))))))
