from edc_visit_schedule import Schedule

from ....crfs import crf_2001, caregiver_crfs_prn, caregiver_crfs_unscheduled, requisitions_prn
from ...schedule_helper import ScheduleHelper
from ..caregiver_visits.cohort_b_visits import visit3001, visit3001sq

# Quarterly Schedules
b_fu_quarterly1_schedule_1 = Schedule(
    name='b_fu_quarterly1_schedule1',
    sequence='4',
    verbose_name='Cohort B(First Child(ren)) FU Quarterly Schedule',
    onschedule_model='flourish_caregiver.onschedulecohortbfuquarterly',
    offschedule_model='flourish_caregiver.caregiveroffschedule',
    consent_model='flourish_caregiver.subjectconsent',
    appointment_model='edc_appointment.appointment'
    )

b_fu_quarterly2_schedule_1 = Schedule(
    name='b_fu_quarterly2_schedule1',
    sequence='4',
    verbose_name='Cohort B(Second Child(ren)) FU Quarterly Schedule',
    onschedule_model='flourish_caregiver.onschedulecohortbfuquarterly',
    offschedule_model='flourish_caregiver.caregiveroffschedule',
    consent_model='flourish_caregiver.subjectconsent',
    appointment_model='edc_appointment.appointment'
    )

b_fu_quarterly3_schedule_1 = Schedule(
    name='b_fu_quarterly3_schedule1',
    sequence='4',
    verbose_name='Cohort B(Third Child(ren)) FU Quarterly Schedule',
    onschedule_model='flourish_caregiver.onschedulecohortbfuquarterly',
    offschedule_model='flourish_caregiver.caregiveroffschedule',
    consent_model='flourish_caregiver.subjectconsent',
    appointment_model='edc_appointment.appointment'
    )

# Generate Quarterly Visits
b_fu_quarterly1_schedule_1.add_visit(visit=visit3001)

schedule_helper1 = ScheduleHelper(visit=visit3001, crfs=crf_2001,
                                  crfs_unscheduled=caregiver_crfs_unscheduled,
                                  requisitions_prn=requisitions_prn,
                                  crfs_prn=caregiver_crfs_prn,
                                  schedule=b_fu_quarterly1_schedule_1)
schedule_helper1.create_quarterly_visits()

visits = b_fu_quarterly1_schedule_1.visits
values = visits.values()

for visit in values:
    b_fu_quarterly2_schedule_1.add_visit(visit=visit)
    b_fu_quarterly3_schedule_1.add_visit(visit=visit)


# Sequential SEC-aims quarterly visits
b_sec_fu_quart1_schedule_1 = Schedule(
    name='b_sec_fu_quart1_schedule1',
    sequence='6',
    verbose_name='Cohort B(First Child(ren)) Sec FU Quarterly Sequential',
    onschedule_model='flourish_caregiver.onschedulecohortbsecseq',
    offschedule_model='flourish_caregiver.caregiveroffschedule',
    consent_model='flourish_caregiver.subjectconsent',
    appointment_model='edc_appointment.appointment'
    )

b_sec_fu_quart1_schedule_1.add_visit(visit=visit3001sq)

# Generate SEC-aims quarterly Visits
schedule_helper = ScheduleHelper(visit=visit3001sq, crfs=crf_2001,
                                 crfs_unscheduled=caregiver_crfs_unscheduled,
                                 requisitions_prn=requisitions_prn,
                                 crfs_prn=caregiver_crfs_prn,
                                 schedule=b_sec_fu_quart1_schedule_1,
                                 postfix='S')

schedule_helper.create_quarterly_visits()

b_sec_fu_quart2_schedule_1 = Schedule(
    name='b_sec_fu_quart2_schedule1',
    sequence='6',
    verbose_name='Cohort B(Second Child(ren)) Sec FU Quarterly Sequential',
    onschedule_model='flourish_caregiver.onschedulecohortbsecseq',
    offschedule_model='flourish_caregiver.caregiveroffschedule',
    consent_model='flourish_caregiver.subjectconsent',
    appointment_model='edc_appointment.appointment'
    )

b_sec_fu_quart3_schedule_1 = Schedule(
    name='b_sec_fu_quart3_schedule1',
    sequence='6',
    verbose_name='Cohort B(Third Child(ren)) Sec FU Quarterly Sequential',
    onschedule_model='flourish_caregiver.onschedulecohortbsecseq',
    offschedule_model='flourish_caregiver.caregiveroffschedule',
    consent_model='flourish_caregiver.subjectconsent',
    appointment_model='edc_appointment.appointment'
    )

# Generate Quarterly Visits
visits = b_sec_fu_quart1_schedule_1.visits
values = visits.values()

for visit in values:
    b_sec_fu_quart2_schedule_1.add_visit(visit=visit)
    b_sec_fu_quart3_schedule_1.add_visit(visit=visit)
