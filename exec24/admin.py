from model import Company


def read_company_data():
    fantasy_name = input('Entre com o nome fantasia da empresa: ')
    social_reason = input('Entre com a razão social da empresa: ')
    company_dict = {"fantasy_name": fantasy_name, "social_reason": social_reason}
    return company_dict


if __name__ == "__main__":
    company_dict = read_company_data()
    new_company = Company(company_dict)
    print('Nome fantasia da empresa: ', new_company.fantasy_name)
    print('Razão social da empresa: ', new_company.social_reason)
