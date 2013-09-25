import os
import unittest

from scrapy.http.response.xml import XmlResponse

from stockcrawler.loaders import ReportLoader


def create_response(filename):
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'sample_data', filename)
    with open(path) as f:
        body = f.read()
    return XmlResponse('file://%s' % path.replace('\\', '/'), body=body)


def parse_xml(filename):
    response = create_response(filename)
    loader = ReportLoader(response=response)
    return loader.load_item()


class TestReportLoader(unittest.TestCase):

    def assert_item(self, item, expected):
        self.assertEqual(item['symbol'], expected['symbol'])
        self.assertEqual(item['doc_type'], expected['doc_type'])
        self.assertEqual(item['period_focus'], expected['period_focus'])
        self.assertEqual(item['end_date'], expected['end_date'])
        self.assertEqual(item['revenues'], expected['revenues'])
        self.assertEqual(item['net_income'], expected['net_income'])
        self.assertEqual(item['eps_basic'], expected['eps_basic'])
        self.assertEqual(item['eps_diluted'], expected['eps_diluted'])
        self.assertEqual(item['dividend'], expected['dividend'])
        self.assertEqual(item['assets'], expected['assets'])
        self.assertEqual(item['equity'], expected['equity'])
        self.assertEqual(item['cash'], expected['cash'])

    def test_goog_20090930(self):
        item = parse_xml('goog-20090930.xml')
        self.assert_item(item, {
            'symbol': 'GOOG',
            'doc_type': '10-Q',
            'period_focus': 'Q3',
            'end_date': '2009-09-30',
            'revenues': 5944851000.0,
            'net_income': 1638975000.0,
            'eps_basic': 5.18,
            'eps_diluted': 5.13,
            'dividend': 0.0,
            'assets': 37702845000.0,
            'equity': 33721753000.0,
            'cash': 12087115000.0
        })

    def test_goog_20120930(self):
        item = parse_xml('goog-20120930.xml')
        self.assert_item(item, {
            'symbol': 'GOOG',
            'doc_type': '10-Q',
            'period_focus': 'Q3',
            'end_date': '2012-09-30',
            'revenues': 14101000000.0,
            'net_income': 2176000000.0,
            'eps_basic': 6.64,
            'eps_diluted': 6.53,
            'dividend': 0.0,
            'assets': 89730000000.0,
            'equity': 68028000000.0,
            'cash': 16260000000.0
        })

    def test_goog_20121231(self):
        item = parse_xml('goog-20121231.xml')
        self.assert_item(item, {
            'symbol': 'GOOG',
            'doc_type': '10-K',
            'period_focus': 'FY',
            'end_date': '2012-12-31',
            'revenues': 50175000000.0,
            'net_income': 10737000000.0,
            'eps_basic': 32.81,
            'eps_diluted': 32.31,
            'dividend': 0.0,
            'assets': 93798000000.0,
            'equity': 71715000000.0,
            'cash': 14778000000.0
        })

    def test_goog_20130630(self):
        item = parse_xml('goog-20130630.xml')
        self.assert_item(item, {
            'symbol': 'GOOG',
            'doc_type': '10-Q',
            'period_focus': 'Q2',
            'end_date': '2013-06-30',
            'revenues': 14105000000.0,
            'net_income': 3228000000.0,
            'eps_basic': 9.71,
            'eps_diluted': 9.54,
            'dividend': 0.0,
            'assets': 101182000000.0,
            'equity': 78852000000.0,
            'cash': 16164000000.0
        })

    def test_msft_20110630(self):
        item = parse_xml('msft-20110630.xml')
        self.assert_item(item, {
            'symbol': 'MSFT',
            'doc_type': '10-K',
            'period_focus': 'FY',
            'end_date': '2011-06-30',
            'revenues': 69943000000.0,
            'net_income': 23150000000.0,
            'eps_basic': 2.73,
            'eps_diluted': 2.69,
            'dividend': 0.64,
            'assets': 108704000000.0,
            'equity': 57083000000.0,
            'cash': 9610000000.0
        })

    def test_ko_20100402(self):
        item = parse_xml('ko-20100402.xml')
        self.assert_item(item, {
            'symbol': 'KO',
            'doc_type': '10-Q',
            'period_focus': 'Q1',
            'end_date': '2010-04-02',
            'revenues': 7525000000.0,
            'net_income': 1614000000.0,
            'eps_basic': 0.70,
            'eps_diluted': 0.69,
            'dividend': 0.44,
            'assets': 47403000000.0,
            'equity': 25157000000.0,
            'cash': 5684000000.0
        })

    def test_ko_20101231(self):
        item = parse_xml('ko-20101231.xml')
        self.assert_item(item, {
            'symbol': 'KO',
            'doc_type': '10-K',
            'period_focus': 'FY',
            'end_date': '2010-12-31',
            'revenues': 35119000000.0,
            'net_income': 11809000000.0,
            'eps_basic': 5.12,
            'eps_diluted': 5.06,
            'dividend': 1.76,
            'assets': 72921000000.0,
            'equity': 31317000000.0,
            'cash': 8517000000.0
        })

    def test_ko_20120928(self):
        item = parse_xml('ko-20120928.xml')
        self.assert_item(item, {
            'symbol': 'KO',
            'doc_type': '10-Q',
            'period_focus': 'Q3',
            'end_date': '2012-09-28',
            'revenues': 12340000000.0,
            'net_income': 2311000000.0,
            'eps_basic': 0.51,
            'eps_diluted': 0.50,
            'dividend': 0.255,
            'assets': 86654000000.0,
            'equity': 33590000000.0,
            'cash': 9615000000.0
        })

    def test_jpm_20090630(self):
        item = parse_xml('jpm-20090630.xml')
        self.assert_item(item, {
            'symbol': 'JPM',
            'doc_type': '10-Q',
            'period_focus': 'Q2',
            'end_date': '2009-06-30',
            'revenues': 25623000000.0,
            'net_income': 1072000000.0,
            'eps_basic': 0.28,
            'eps_diluted': 0.28,
            'dividend': 0.05,
            'assets': 2026642000000.0,
            'equity': 154766000000.0,
            'cash': 25133000000.0
        })

    def test_xom_20111231(self):
        item = parse_xml('xom-20111231.xml')
        self.assert_item(item, {
            'symbol': 'XOM',
            'doc_type': '10-K',
            'period_focus': 'FY',
            'end_date': '2011-12-31',
            'revenues': 467029000000.0,
            'net_income': 41060000000.0,
            'eps_basic': 8.43,
            'eps_diluted': 8.42,
            'dividend': 1.85,
            'assets': 331052000000.0,
            'equity': 160744000000.0,
            'cash': 12664000000.0
        })

    def test_omx_20110924(self):
        item = parse_xml('omx-20110924.xml')
        self.assert_item(item, {
            'symbol': 'OMX',
            'doc_type': '10-Q',
            'period_focus': 'Q3',
            'end_date': '2011-09-24',
            'revenues': 1774767000.0,
            'net_income': 21518000.0,
            'eps_basic': 0.25,
            'eps_diluted': 0.25,
            'dividend': 0.0,
            'assets': 4002981000.0,
            'equity': 657636000.0,
            'cash': 485426000.0
        })

    def test_aapl_20100626(self):
        item = parse_xml('aapl-20100626.xml')
        self.assert_item(item, {
            'symbol': 'AAPL',
            'doc_type': '10-Q',
            'period_focus': 'Q3',
            'end_date': '2010-06-26',
            'revenues': 15700000000.0,
            'net_income': 3253000000.0,
            'eps_basic': 3.57,
            'eps_diluted': 3.51,
            'dividend': 0.0,
            'assets': 64725000000.0,
            'equity': 43111000000.0,
            'cash': 9705000000.0
        })

    def test_jnj_20120930(self):
        item = parse_xml('jnj-20120930.xml')
        self.assert_item(item, {
            'symbol': 'JNJ',
            'doc_type': '10-Q',
            'period_focus': 'Q3',
            'end_date': '2012-09-30',
            'revenues': 17052000000.0,
            'net_income': 2968000000.0,
            'eps_basic': 1.08,
            'eps_diluted': 1.05,
            'dividend': 0.61,
            'assets': 118951000000.0,
            'equity': 63761000000.0,
            'cash': 15486000000.0
        })
