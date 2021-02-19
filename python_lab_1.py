from Parfums import Parfums
if __name__ == '__main__':
    parfum_encre = Parfums("Деревинний аромат","Lalique",["кипарис","ветивер","кашемірове дерево","мускус"])
    print(parfum_encre)
    Parfums.static_method(Parfums.fragnance_author)
    parfum_guerlain = Parfums("","GUERLAIN",["лаванда", "бергамот","Жасмин","ваніль"],"Mon Guerlain",50,2090)
    print(parfum_guerlain)
    parfum_unique  = Parfums("","",["рожевий перець","лаванда","герань"],"Unique Wood",75,2250)
    print(parfum_unique)