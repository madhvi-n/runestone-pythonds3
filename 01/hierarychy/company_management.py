"""
Class hierarchy for company management
"""

class Company:
    def __init__(self, company_name, location):
        self.company_name = company_name
        self.location = location

    def __str__(self):
        return f"Company: {self.company_name}, {self.location}"

    def __repr(self):
        return f"Company: {self.company_name}, {self.location}"


class Management(Company):
    def __init__(self, company_name, location, employee, position, management_type, **kwargs):
        self.management_type = management_type
        self.employee = employee
        self.position = position
        super().__init__(company_name, location)

    def __str__(self):
        return f"{self.employee}: {self.position} in {self.management_type} management at {self.company_name}"

    def __repr__(self):
        return f"{self.employee}: {self.position} in {self.management_type} management at {self.company_name}"

    def type(self):
        return f"{self.management_type}"

    def position(self):
        return f"{self.position}"


class TopLevelManagement(Management):
    def __init__(self, company_name, location, employee, position, **kwargs):
        super().__init__(company_name, location, employee, position, management_type='Top level', **kwargs)

    @classmethod
    def chairman(cls) -> 'TopLevelManagement':
        return cls('Xamarin Ltd', 'John Doe', 'Chairman', 'United States')

    @classmethod
    def vice_president(cls) -> 'TopLevelManagement':
        return cls('Xamarin Ltd', 'Jane Doe', 'Vice President', 'United States')

    @classmethod
    def ceo(cls) -> 'TopLevelManagement':
        return cls('Xamarin Ltd', 'Jeanne Donne', 'CEO', 'United States')


class MiddleManagement(Management):
    def __init__(self, company_name, location, employee, position, **kwargs):
        super().__init__(company_name, location, employee, position, management_type='Middle', **kwargs)

    @classmethod
    def general_manager(cls) -> 'MiddleManagement':
        return cls('Xamarin Ltd', 'Aran Diego', 'General Manager', 'United States')

    @classmethod
    def regional_manager(cls) -> 'MiddleManagement':
        return cls('Xamarin Ltd', 'Antuan Doe', 'General Manager', 'United States')


class FirstLineManagement(Management):
    def __init__(self, company_name, location, employee, position, **kwargs):
        super().__init__(company_name, location, employee, position, management_type='First line', **kwargs)

    @classmethod
    def supervisor(cls) -> 'FirstLineManagement':
        return cls('Xamarin Ltd', 'Sam Pauline', 'Supervisor', 'United States')

    @classmethod
    def office_manager(cls) -> 'FirstLineManagement':
        return cls('Xamarin Ltd', 'Sarah Jones', 'Office Manager', 'United States')

    @classmethod
    def team_leader(cls) -> 'FirstLineManagement':
        return cls('Xamarin Ltd', 'Amy Joe', 'Team Leader', 'United States')


def main():
    company = Company('Xamarin Ltd', 'United States')
    print(company)

    chairman = TopLevelManagement.chairman()
    print(chairman)

    ceo = TopLevelManagement.ceo()
    print(ceo)

    general_manager = MiddleManagement.general_manager()
    print(general_manager)

    regional_manager = MiddleManagement.regional_manager()
    print(regional_manager)

    supervisor = FirstLineManagement.supervisor()
    print(supervisor)

    office_manager = FirstLineManagement.office_manager()
    print(office_manager)

    team_leader = FirstLineManagement.team_leader()
    print(team_leader)


if __name__ == '__main__':
    main()
