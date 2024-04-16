{#
This macro return the formal name of each item
#}

{% macro province_name(province) -%}

    case cast ({{ province }} as string)
        when "buenos_aires" then "Buenos Aires"
        when "pba" then "Buenos Aires"
        when "catamarca" then "Catamarca"
        when "chaco" then "Chaco"
        when "chubut" then "Chubut"
        when "ciudad_de_buenos_aires" then "CABA"
        when "caba" then "CABA"
        when "cordoba" then "Cordoba"
        when "corrientes" then "Corrientes"
        when "entre_rios" then "Entre Rios"
        when "formosa" then "Formosa"
        when "jujuy" then "Jujuy"
        when "la_pampa" then "La Pampa"
        when "la_rioja" then "La Rioja"
        when "mendoza" then "Mendoza"
        when "misiones" then "Misiones"
        when "neuquen" then "Neuquen"
        when "rio_negro" then "Rio Negro"
        when "salta" then "Salta"
        when "san_juan" then "San Juan"
        when "san_juan_zf_zonamerica_ex_montevideo" then "Zonamerica"
        when "san_luis" then "San Luis"
        when "santa_cruz" then "Santa Cruz"
        when "santa_fe" then "Santa Fe"
        when "santiago_del_estero" then "Santiago del Estero"
        when "tucuman" then "Tucuman"
        when "tierra_del_fuego" then "Tierra del Fuego"
        when "extranjero" then "Extranjero"
        when "plataforma_continental" then "Plataforma Continental"
        when "indeterminado" then "Sin Determinar"
        when "" then "Total"
        when "exportaciones_totales" then "Total"
    end

{%- endmacro %}

{% macro category_name(category) -%}

    case cast({{category}} as string)
        when "pp" then "Productos Primarios"
        when "moa" then "Manufacturas de Origen Agropecuario"
        when "moi" then "Manufacturas de Origen Industrial"
        when "cye" then "Combustibles y Energia"
    end


{%- endmacro %}

{% macro destination_name (destination)%}

    case cast ({{destination}} as string)
        when "brasil" then "Brasil"
        when "estados_unidos" then "EEUU"
        when "chile" then "Chile"
        when "china" then "China"
        when "uruguay" then "Uruguay"
        when "paraguay" then "Paraguay"
        when "mexico" then "Mexico"
        when "paises_bajos" then "Paises Bajos"
        when "alemania" then "Alemania"
        when "venezuela" then "Venezuela"
        when "resto" then "Resto del mundo"
        when "japon" then "Japon"
        when "republica_corea" then "Corea del Sur"
        when "espania" then "España"
        when "finlandia" then "Finlandia"
        when "filipinas" then "Filipinas"
        when "bulgaria" then "Bulgaria"
        when "canada" then "Canada"
        when "india" then "India"
        when "italia" then "Italia"
        when "indonesia" then "Indonesia"
        when "egipto" then "Egipto"
        when "colombia" then "Colombia"
        when "hong_kong" then "Hong Kong"
        when "vietnam" then "Vietnam"
        when "iraq" then "Irak"
        when "rusia" then "Rusia"
        when "francia" then "Francia"
        when "sudafrica" then "Sudafrica"
        when "bolivia" then "Bolivia"
        when "suiza" then "Suiza"
        when "zf_zonamerica_ex_montevideo_uru" then "Zonamerica"
        when "malasia" then "Malasia"
        when "costa_rica" then "Costa Rica"
        when "indet_continente" then "Sin determinar"
        when "reino_unido" then "Reino Unido"
        when "argelia" then "Argelia"
        when "peru" then "Peru"
        when "belgica" then "Belgica"
        when "ecuador" then "Ecuador"
        when "siria" then "Siria"
        when "arabia_saudita" then "Arabia Saudita"
        end

{% endmacro %}

