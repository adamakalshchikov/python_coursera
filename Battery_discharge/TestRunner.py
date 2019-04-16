# -*- coding: cp1251 -*-
import doctest
import logging

#LOG_FORMAT = u'%(levelname)-8s [%(asctime)s] %(message)s'
LOG_FORMAT = u'8s [%(asctime)s] %(message)s'

class LowBattery(Exception): pass
class PaperMissing(Exception): pass


class TetRunner:

    def __init__(self, drv, test_sample=None, sample_description=None, use_description=False):
        """
        ���

        drv - ������ ��������;
        test_sample - ����� ������� ��� (int) ;
        sample_descriptoin - �������� ��� (str) ;
        use_description - ��������� �������� (������� �� None) � ����� �� ��������� (boolean) ;

        >>>>from common_OT import wrapper_dto
        >>>driver = wrapper_dto.dto()
        >>>battery = TetRunner(driver)


        >>>>battery = TetRunner(driver, test_sample=1, sample_description="ICR18650 Supreme", use_description=True)
        """
        self.__drv = drv
        self.__sample = test_sample
        self.__battery_description = sample_description
        self.__use_desc = use_description

    @staticmethod
    def create_log(self, filename=None):
        """
        ������ ���
        :param filename: ��� ��� - �����, ���� None - ��������������� ����������� ���
        :return: None
        """

        logging.basicConfig(format=LOG_FORMAT, level=logging.DEBUG,
                            file=filename if not None else u'Battery_test' + self.__sample + u'.csv')

    @staticmethod
    def