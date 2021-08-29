import bh1750fvi
from machine import Pin, I2C

# I2C (D1=Pin5=SCL, D2=Pin4=SDA): LCD1602, BH1750, MPU6050

i2c = I2C(scl=Pin(5), sda=Pin(4))

def bh1750_read():
    return bh1750fvi.sample(i2c)

def main():      
  light = bh1750_read()
  print(light)
           
if __name__ == "__main__":
    main()
