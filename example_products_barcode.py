from generate_barcode import generate

products = {
    "Feijão": "551746511111",
    "Arroz": "323523222345",
    "Macarrão": "938273339523",
    "Azeite": "432837884234",
}

for product in products:
    generate(
        code=products[product],
        output="produtos",
        filename=product
    )
