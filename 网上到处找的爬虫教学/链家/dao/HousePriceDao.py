
import MySQLdb



def insertOneHouseInfo(HouseInfo):
    db = MySQLdb.connect("localhost", "root", "", "spiderpy", charset='utf8')
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    sql ="insert into  houseinfo(selling_house_number,trade_number_last90day,house_avg_price,increase_house,increase_people,people_seehouse_number) values(%s,%s,%s,%s,%s,%s)"
    val=(HouseInfo.selling_house_number,HouseInfo.trade_number_last90day,HouseInfo.house_avg_price,HouseInfo.increase_house,HouseInfo.increase_people,HouseInfo.people_seehouse_number)
    print(val)

    cursor.execute(sql,val)
    # 提交到数据库执行
    db.commit()
    db.close

