library(magrittr)
library(purrr)
library(stringr)
library(dplyr)
library(tidyr)

df <- readLines('2.in') %>%
  map_dfr(~ str_match(.x, "^(.*?)-(.*?)\\s(.*?)\\:\\s(.*?)$") %>%
			  set_names(c('string', 'n1', 'n2', 'l', 'pwd'))) %>%
  mutate(n1 = as.integer(n1), n2 = as.integer(n2))

df %>%
  mutate(letter_count = str_count(pwd, l)) %>%
  filter(n1 <= letter_count & letter_count <= n2) %>%
  nrow() %>% 
  print()

df %>%
  mutate(pos1 = substr(pwd, n1, n1),
         pos2 = substr(pwd, n2, n2),
         valid = xor(pos1 == l, pos2 == l)) %>%
  filter(valid) %>%
  nrow() %>%
  print()

