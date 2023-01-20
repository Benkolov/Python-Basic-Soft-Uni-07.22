price_scumria = float(input())
price_caca = float(input())
palamud = float(input())
safrid = float(input())
midi = int(input())

price_palamud_kg = price_scumria * 1.60
price_safrid_kg = price_caca * 1.80
price_midi_kg = 7.50

total_price = (price_palamud_kg * palamud) + (price_safrid_kg * safrid) + (price_midi_kg * midi)

print(f"{total_price:.2f}")