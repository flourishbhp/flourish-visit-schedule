from dateutil.relativedelta import relativedelta
from edc_visit_schedule import Visit as BaseVisit
from flourish_visit_schedule.visit_schedules.crfs import bc_crf_2000, crf_2001, crf_3000

from ....crfs import caregiver_crfs_prn


class Visit(BaseVisit):

    def __init__(self, crfs_unscheduled=None, requisitions_unscheduled=None,
                 crfs_prn=None, requisitions_prn=None,
                 allow_unscheduled=None, **kwargs):
        super().__init__(
            allow_unscheduled=True if allow_unscheduled is None else allow_unscheduled,
            crfs_unscheduled=crfs_unscheduled,
            requisitions_unscheduled=requisitions_unscheduled,
            crfs_prn=crfs_prn,
            requisitions_prn=requisitions_prn,
            **kwargs)


visit2000 = Visit(
    code='2000M',
    title='Cohort B Enrollment Visit',
    timepoint=0,
    rbase=relativedelta(days=0),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=30),
    requisitions=None,
    crfs=bc_crf_2000,
    facility_name='5-day clinic')

visit2001 = Visit(
    code='2001M',
    title='Cohort B Quarterly Visit 1',
    timepoint=1,
    rbase=relativedelta(days=90),
    rlower=relativedelta(days=45),
    rupper=relativedelta(days=44),
    requisitions=None,
    crfs=crf_2001,
    crfs_prn=caregiver_crfs_prn,
    facility_name='5-day clinic')

visit3000 = Visit(
    code='3000M',
    title='Cohort B Follow Up Visit',
    timepoint=14,
    rbase=relativedelta(days=0),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=30),
    requisitions=None,
    crfs=crf_3000,
    facility_name='5-day clinic')

visit3001 = Visit(
    code='3001M',
    title='Cohort B Follow Up Quarterly Visit 1',
    timepoint=2,
    rbase=relativedelta(days=90),
    rlower=relativedelta(days=45),
    rupper=relativedelta(days=44),
    requisitions=None,
    crfs=crf_2001,
    crfs_prn=caregiver_crfs_prn,
    facility_name='5-day clinic')
