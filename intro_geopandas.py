#Replicar el ejemplo, agregando los elementos propuestos 
import geopandas as gpd 

from cargar_archivo import cargar_archivo

from mostrar_info import mostrar_info

from mostrar_mapa import mostrar_mapa

from mostrar_datos import mostrar_datos

my_gdf = cargar_archivo("barriolegalizado.json")

#Mostrar información del gdf
mostrar_info(my_gdf)

#Crear una funcion para mostrar el mapa de la geoserie del gdf
mostrar_mapa(my_gdf)

#Trabajar con datos del geodataframe 
mostrar_datos(my_gdf)
