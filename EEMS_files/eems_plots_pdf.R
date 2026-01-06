### Platy results eems deme 200 com 20M de iterações ####
library(rEEMSplots)
Sys.setenv(R_GSCMD="C:/Program Files/gs/gs9.53.1/bin/gswin64c.exe")
# Use the provided example or supply the path to your own EEMS run.
platydata_path <- getwd()

eems_results <- file.path(platydata_path, c("platy_eems_chain1","platy_eems_chain12","platy_eems_chain13") )
name_figures <- file.path(platydata_path, "platy_eems_finald700pdf")
library("rgdal")
projection_none <- "+proj=longlat +datum=WGS84"
projection_mercator <- "+proj=merc +datum=WGS84"
library("rworldmap")
library("rworldxtra")
library("RColorBrewer")
##Add arbitrary graphical elements (points, lines, etc)
library("rgdal") ## Defines functions to transform spatial elements
library("rworldmap") ## Defines world map

projection_none <- "+proj=longlat +datum=WGS84"
projection_mercator <- "+proj=merc +datum=WGS84"
#### Add the map of America explicitly by passing the shape file # mapafinal RODAS ESSE PARA PDF
map_world <- getMap()
map_america <- map_world[which(map_world@data$continent == "South America"), ]
plot(map_america)
eems.plots(mcmcpath = eems_results,
           plotpath = paste0(name_figures, "-shapefile"),
           longlat = TRUE,
           out.png = FALSE,
           m.plot.xy = {plot(map_america, col = NA, add = TRUE)},
           q.plot.xy = {plot(map_america, col = NA, add = TRUE)})
