field_name_map = {
    "_id": "id",
    "x_wgs84": "x",
    "y_wgs84": "y",
    "x_pl2000": "x_pl",
    "y_pl2000": "y_pl",
    "numer_inw": "inventory_number",
    "dzielnica": "district",
    "jednostka": "unit",
    "miasto": "city",
    "adres": "address",
    "numer_adres": "property_number",
    "lokalizacja": "location",
    "gatunek": "species",
    "gatunek_1": "species_lat",
    "data_wyk_pom": "measurement_date",
    "wiek_w_dni": "age_d",
    "wysokosc": "height_m",
    "pnie_obwod": "stem_circumference",
    "srednica_k": "crown_diameter",
    "stan_zdrowia": "health_state"
}

health_state = {
    "dobry": "good",
    "średni": "medium",
    "zły": "bad"
}


def transform_service_dict(service_tree: dict[str, str]) -> dict[str, str]:
    res = {}
    try:
        for key, value in service_tree.items():
            if key == "stan_zdrowia":
                res[field_name_map[key]] = health_state[value]
            else:
                res[field_name_map[key]] = value
    except Exception as e:
        print(f"Error while parsing {service_tree}", e)

    return res
