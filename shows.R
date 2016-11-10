library(ggplot2)
bbi<-element_text(face="bold.italic", color="black")

friends <- read.csv("~/Desktop/friends.csv")
seinfeld <- read.csv("~/Desktop/seinfeld.csv")
shows <- read.csv("~/Desktop/nyshows.csv")

graph.friends <- ggplot(friends, aes(label=name, x=men, y=women, col=difference)) +
  geom_point(size=2.5, alpha=1) +
  scale_colour_gradient2(low="magenta4", mid="gray", high="dodgerblue3", midpoint = 0) +
  xlim(3,10) + ylim(3,10) + xlab("Average Male Rating") + ylab("Average Female Rating") + 
  labs(title="Friends Episode Ratings by Gender") + theme(title=bbi) + 
  annotate("text", x = 4, y = 9, label = "Male Average: 8.40\n Female Average: 8.44\nr=0.96") +
  geom_text(nudge_x = c(rep(c(-0.5,0.8),118)), nudge_y=-0.18)

graph.sein <- ggplot(seinfeld, aes(label=name, x=men, y=women, col=difference)) +
  geom_point(size=2.5, alpha=1) +
  scale_colour_gradient2(low="magenta4", mid="gray", high="dodgerblue3", midpoint = 0) +
  xlim(3,10) + ylim(3,10) + xlab("Average Male Rating") + ylab("Average Female Rating") + 
  labs(title="Seinfeld Episode Ratings by Gender") + theme(title=bbi) + 
  annotate("text", x = 4, y = 9, label = "Male Average: 8.48\n Female Average: 7.99\nr=0.67") +
  geom_text(nudge_x = seinfeld$horz, nudge_y=seinfeld$vert)

graph.all <- ggplot(shows, aes(label=label, x=maverage, y=faverage, col=difference)) +
  geom_point(aes(shape = factor(lead)), size=4) +
  scale_colour_gradient2(low="magenta4", mid="gray", high="dodgerblue3", midpoint = 0) +
  xlim(5,10) + ylim(5,10) + xlab("Average Male Rating") + ylab("Average Female Rating") + 
  labs(title="NYC Sitcoms since 1990", shape="lead") + 
  theme(title=bbi) +
  geom_text(size=3, nudge_y=0.1, color="black")