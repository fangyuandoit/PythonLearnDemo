class HouseInfo:
       id=-1
       selling_house_number=""
       trade_number_last90day=""
       house_avg_price=""
       increase_house=""
       increase_people=""
       people_seehouse_number=""
       create_time=""

       def toString(self) -> str:
              return str(
                     self.id) + "    " + self.selling_house_number + "    " + self.trade_number_last90day + "    " + self.house_avg_price + "    " + self.increase_house+ "    " + self.increase_people+ "    " + self.people_seehouse_number + "  " + self.create_time

