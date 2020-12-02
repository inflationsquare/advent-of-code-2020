library(magrittr)

readLines('1-1.in') %>%
	as.integer() %>%
	combn(2) %>% 
	{.[, colSums(.) == 2020]} %>% 
	prod() %>% 
	print()
