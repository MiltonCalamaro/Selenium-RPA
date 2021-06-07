import sys
import unittest
import time
import pandas as pd
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestReto1(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

    def tearDown(self) -> None:
        self.driver.close()
    
    #@unittest.skip("temp")    
    def test_reto1(self):
        driver = self.driver
        link = 'https://www.resultadossep.eleccionesgenerales2021.pe/SEP2021/EleccionesPresidenciales/RePres/T'
        driver.get(link)
        
        ambito_peru = driver.find_element_by_xpath('//*[@id="select_ambito"]/option[contains(text(), "PERÚ")]')
        ambito_peru.click()

        box = f'//following-sibling::select/option'     
        departamento_label = driver.find_elements_by_xpath('//label[contains(text(), "Departamento")]'+box)
        list_departamentos = [i.text for i in departamento_label]
        list_departamentos.remove('--TODOS--')
        def get_info_elecciones(list_departamentos):
            list_dict = []
            for departamento in list_departamentos:
                print(departamento)
                dict_ = {}
                if departamento!='ICA':
                    box = f'//following-sibling::select/option[contains(text(),"{departamento}")]'     
                    departamento_box = driver.find_element_by_xpath('//label[contains(text(), "Departamento")]'+box)
                    departamento_box.click()
                else:
                    x_path ='/html/body/onpe-root/onpe-layout-container/onpe-onpe-epres-re/div[1]/div[3]/div[1]/div[1]/div/div/div[2]/select/option[12]'
                    departamento_box = driver.find_element_by_xpath(x_path)
                    departamento_box.click()

                time.sleep(3)
                elecHabiles = driver.find_element_by_id('elecHabiles')
                porPartCiudadana = driver.find_element_by_id('porPartCiudadana')
                porPartCiudadanapor = driver.find_element_by_id('porPartCiudadanapor')
                porActasProcesadas = driver.find_element_by_id('porActasProcesadas')
                voto_valido_castillo = driver.find_element_by_xpath('//*[contains(text(), "PARTIDO POLITICO NACIONAL PERU LIBRE")]'
                                                                    +'//following-sibling::td')

                voto_valido_keiko = driver.find_element_by_xpath('//*[contains(text(), "FUERZA POPULAR")]'
                                                                    +'//following-sibling::td')
                
                dict_['departamento'] = departamento
                dict_['electores_abiles'] = elecHabiles.text
                dict_['part_ciudadana'] = porPartCiudadana.text
                dict_['part_ciudadana_porc'] = porPartCiudadanapor.text
                dict_['actas_procesadas_porc'] = porActasProcesadas.text
                dict_['voto_valido_castillo'] = voto_valido_castillo.text
                dict_['voto_valido_keiko'] = voto_valido_keiko.text

                list_dict.append(dict_)
            return pd.DataFrame(list_dict)
        df = get_info_elecciones(list_departamentos)


        df['part_ciudadana_porc'] = df.apply( lambda row: float(row['part_ciudadana_porc'].split()[0]), axis=1)
        df['actas_procesadas_porc'] = df.apply(lambda row: float(row['actas_procesadas_porc'].split()[0]), axis=1)
        df['voto_castillo_porc'] = df.apply(lambda row: round(int(row['voto_valido_castillo'].replace(',',''))/ 
                                                           (int(row['voto_valido_keiko'].replace(',',''))+
                                                            int(row['voto_valido_castillo'].replace(',',''))), 4)*100
                                                                        , axis=1)
        df['voto_keiko_porc'] = df.apply(lambda row: round(int(row['voto_valido_keiko'].replace(',',''))/ 
                                                           (int(row['voto_valido_keiko'].replace(',',''))+
                                                            int(row['voto_valido_castillo'].replace(',',''))), 4)*100
                                                                        , axis=1)

        df = df.sort_values('actas_procesadas_porc', ascending=False)
        df.index = range(len(df))
        df.to_csv('df_elecciones_peru.csv', index=False, sep='|')
        print(df)

    #@unittest.skip("temp")
    def test_reto2(self):
        driver = self.driver
        link = 'https://www.resultadossep.eleccionesgenerales2021.pe/SEP2021/EleccionesPresidenciales/RePres/T'
        driver.get(link)
        ambito_extranjero = driver.find_element_by_xpath('//*[@id="select_ambito"]/option[contains(text(), "EXTRANJERO")]')
        ambito_extranjero.click()

        box = f'//following-sibling::select/option'     
        departamento_label = driver.find_elements_by_xpath('//label[contains(text(), "Continente")]'+box)
        list_continente = [i.text for i in departamento_label]
        list_continente.remove('--TODOS--')


        def get_info_elecciones(list_continente):
            list_dict = []
            for continente in list_continente:
                print(continente)
                dict_ = {}
                box = f'//following-sibling::select/option[contains(text(),"{continente}")]'     
                continente_box = driver.find_element_by_xpath('//label[contains(text(), "Continente")]'+box)
                continente_box.click()
                elecHabiles = driver.find_element_by_id('elecHabiles')
                porPartCiudadana = driver.find_element_by_id('porPartCiudadana')
                porPartCiudadanapor = driver.find_element_by_id('porPartCiudadanapor')
                porActasProcesadas = driver.find_element_by_id('porActasProcesadas')

                voto_valido_castillo = driver.find_element_by_xpath('//*[contains(text(), "PARTIDO POLITICO NACIONAL PERU LIBRE")]'
                                                                    +'//following-sibling::td')

                voto_valido_keiko = driver.find_element_by_xpath('//*[contains(text(), "FUERZA POPULAR")]'
                                                                    +'//following-sibling::td')
                dict_['continente'] = continente
                dict_['electores_abiles'] = elecHabiles.text
                dict_['part_ciudadana'] = porPartCiudadana.text
                dict_['part_ciudadana_porc'] = porPartCiudadanapor.text
                dict_['actas_procesadas_porc'] = porActasProcesadas.text
                dict_['voto_valido_castillo'] = voto_valido_castillo.text
                dict_['voto_valido_keiko'] = voto_valido_keiko.text
                list_dict.append(dict_)
            return pd.DataFrame(list_dict)
        df = get_info_elecciones(list_continente)

        df['part_ciudadana_porc'] = df.apply( lambda row: float(row['part_ciudadana_porc'].split()[0]), axis=1)
        df['actas_procesadas_porc'] = df.apply(lambda row: float(row['actas_procesadas_porc'].split()[0]), axis=1)

        df['voto_castillo_porc'] = df.apply(lambda row: round(int(row['voto_valido_castillo'].replace(',',''))/ 
                                                           (int(row['voto_valido_keiko'].replace(',',''))+
                                                            int(row['voto_valido_castillo'].replace(',',''))), 4)*100
                                                                        , axis=1)
        df['voto_keiko_porc'] = df.apply(lambda row: round(int(row['voto_valido_keiko'].replace(',',''))/ 
                                                           (int(row['voto_valido_keiko'].replace(',',''))+
                                                            int(row['voto_valido_castillo'].replace(',',''))), 4)*100
                                                                        , axis=1)

        df = df.sort_values('actas_procesadas_porc', ascending=False)
        df.index = range(len(df))
        df.to_csv('df_elecciones_extranjero.csv', index=False, sep='|')
        print(df)

if __name__ == '__main__':
    unittest.main()