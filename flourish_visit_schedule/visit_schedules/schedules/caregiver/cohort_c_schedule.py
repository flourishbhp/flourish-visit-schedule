from dateutil.relativedelta import relativedelta
from edc_visit_schedule import Schedule, Visit

from ..schedule_helper import ScheduleHelper
from ...crfs import bc_crf_1000, crf_3000, crf_4000

cohort_c_schedule_1 = Schedule(
    name='cohort_c_schedule1',
    verbose_name='Cohort C Schedule V1',
    onschedule_model='flourish_caregiver.onschedulecohortc1',
    offschedule_model='flourish_caregiver.caregiveroffschedule',
    consent_model='flourish_caregiver.subjectconsent',
    appointment_model='edc_appointment.appointment'
    )

visit1000 = Visit(
    code='1000M',
    title='Cohort C Enrollment Visit',
    timepoint=0,
    rbase=relativedelta(days=0),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=None,
    crfs=bc_crf_1000,
    facility_name='5-day clinic')

visit3000 = Visit(
    code='3000M',
    title='Cohort C Quarterly Visit',
    timepoint=1,
    rbase=relativedelta(months=3),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=None,
    crfs=crf_3000,
    facility_name='5-day clinic')

visit4000 = Visit(
    code='4000M',
    title='Cohort C Follow Up Visit',
    timepoint=12,
    rbase=relativedelta(years=3),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=None,
    crfs=crf_4000,
    facility_name='5-day clinic')

schedule_helper = ScheduleHelper(visit=visit3000, crfs=crf_3000,
                                 schedule=cohort_c_schedule_1, visit4000=visit4000)
schedule_helper.create_quarterly_visits()

cohort_c_schedule_1.add_visit(visit=visit1000)
cohort_c_schedule_1.add_visit(visit=visit3000)
cohort_c_schedule_1.add_visit(visit=visit4000)

""" Extra schedules for mothers with more that one child participation. """
cohort_c2_schedule_1 = Schedule(
    name='cohort_c2_schedule1',
    verbose_name='Cohort C Schedule2 V1',
    onschedule_model='flourish_caregiver.onschedulecohortc2',
    offschedule_model='flourish_caregiver.caregiveroffschedule',
    consent_model='flourish_caregiver.subjectconsent',
    appointment_model='edc_appointment.appointment'
    )

cohort_c3_schedule_1 = Schedule(
    name='cohort_c3_schedule1',
    verbose_name='Cohort C Schedule3 V1',
    onschedule_model='flourish_caregiver.onschedulecohortc3',
    offschedule_model='flourish_caregiver.caregiveroffschedule',
    consent_model='flourish_caregiver.subjectconsent',
    appointment_model='edc_appointment.appointment'
    )

visits = cohort_c_schedule_1.visits
values = visits.values()

for visit in values:
    cohort_c2_schedule_1.add_visit(visit=visit)
    cohort_c3_schedule_1.add_visit(visit=visit)