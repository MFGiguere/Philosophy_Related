library (tidyverse)
setwd('FilePath')

#This read the 3 csv files I have and filter some datas for later on. Datas were collected using my Concepts.py script. 
df <- read.table('Datas3.csv', header = FALSE, sep=';', col.names = c('Virchow', 'Annee', 'Textes'), fileEncoding="UTF-8-BOM")
df2 <- read.table('Datas2.csv', header = FALSE, sep=';', col.names = c('Virchow', 'Annee', 'Textes'), fileEncoding="UTF-8-BOM")
df4 <- read.table('Datas4.csv', header = FALSE, sep=';', col.names = c('Virchow', 'Annee', 'Types', 'Nv'), fileEncoding="UTF-8-BOM")
df3 <- df4 %>%
  filter(Virchow>1)
df5 <- df3 %>%
  filter((Virchow>2& Types=='Articles')|(Virchow>9 & Types=='Monographies' & Annee!=2008)|(Virchow>3 & Types=='Reviews'))

#This is the main graph i'm using to present my datas in my masters thesis. 
virc2 <- ggplot(data=df4, mapping = aes(x=Annee, y=Virchow, color=Types)) +
  geom_line(size=1)+ 
  geom_point(color='black', alpha=0.75, aes(size=Nv)) +
  geom_text(data=df3, aes(label=Virchow), nudge_x=3.5, color='black') +
  geom_text(data=df5, aes(label=Annee), vjust = -1.2, color='black') +
  facet_wrap(~Types, nrow=1) + 
  guides(color = 'none', size='none')

#This was a different way of presenting the datas that I didn't use. 
virc <- ggplot(mapping = aes(x=Annee, y=Virchow, alpha='0,5'), fill='grey') +
  geom_area(data=df, size=1, color='blue') +
  geom_area(data= df2, size=1, color='darkgreen') +
  geom_text(data=df3, aes(label=Virchow, alpha='1'), vjust = -1.5) +
  guides(alpha = 'none')

#Clearning up and presenting datas. 
labelled <- virc2 +
  theme_bw() +
  labs(
    x = "Années de publication",
    y = "Nombre de mentions",
    title = "Mentions de Virchow dans les textes szasziens"
  )
labelled

