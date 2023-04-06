def update_car_info(**car):
    info =(
        f"{car['brand']}"
        f"{car[ 'price']}"
        f"{car[ 'is_avalaible']}"
    )
    return info
info = update_car_info(brand= 'BMW', price= 20000, is_avalaible= True  )
print(info)
