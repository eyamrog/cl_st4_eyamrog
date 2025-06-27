/* ANOVA - CL_St4_Ph1_eyamrog_ANOVA */
/* Replace all occurrences of this project ID by yours and create a folder named after it */
%let project = cl_st4_ph1_eyamrog_ANOVA;

%let myfolder = &project;

/* Replace all occurrences of this user ID by yours */
%let sasusername = u63529080;

/* Importing the data set */
proc import datafile="/home/&sasusername/&myfolder/df_cl_st1_eyamrog_dimensions_sas.tsv"
            out=cl_st4_ph1_eyamrog_ANOVA
            dbms=tab
            replace;
   getnames=yes;
run;

/* ANOVA - Dimension 1 by Source */

title "ANOVA for &project - Dimension 1 by Source";
ods noproctitle;
ods graphics / imagemap=on;

proc glm data=WORK.CL_ST4_PH1_EYAMROG_ANOVA;
    class Source;
    model 'Dimension 1'n = Source;
    means Source;
run;
quit;

/* ANOVA - Dimension 2 by Source */

title "ANOVA for &project - Dimension 2 by Source";
ods noproctitle;
ods graphics / imagemap=on;

proc glm data=WORK.CL_ST4_PH1_EYAMROG_ANOVA;
    class Source;
    model 'Dimension 2'n = Source;
    means Source;
run;
quit;

/* ANOVA - Dimension 3 by Source */

title "ANOVA for &project - Dimension 3 by Source";
ods noproctitle;
ods graphics / imagemap=on;

proc glm data=WORK.CL_ST4_PH1_EYAMROG_ANOVA;
    class Source;
    model 'Dimension 3'n = Source;
    means Source;
run;
quit;

/* ANOVA - Dimension 4 by Source */

title "ANOVA for &project - Dimension 4 by Source";
ods noproctitle;
ods graphics / imagemap=on;

proc glm data=WORK.CL_ST4_PH1_EYAMROG_ANOVA;
    class Source;
    model 'Dimension 4'n = Source;
    means Source;
run;
quit;

/* ANOVA - Dimension 5 by Source */

title "ANOVA for &project - Dimension 5 by Source";
ods noproctitle;
ods graphics / imagemap=on;

proc glm data=WORK.CL_ST4_PH1_EYAMROG_ANOVA;
    class Source;
    model 'Dimension 5'n = Source;
    means Source;
run;
quit;

/* ANOVA - Dimension 1 by Source by Discipline */

title "ANOVA for &project - Dimension 1 by Source by Discipline";
ods noproctitle;
ods graphics / imagemap=on;

proc glm data=WORK.CL_ST4_PH1_EYAMROG_ANOVA;
    class Source Discipline;
    model 'Dimension 1'n = Source Discipline Source*Discipline;
    means Source*Discipline;
run;
quit;

/* ANOVA - Dimension 2 by Source by Discipline */

title "ANOVA for &project - Dimension 2 by Source by Discipline";
ods noproctitle;
ods graphics / imagemap=on;

proc glm data=WORK.CL_ST4_PH1_EYAMROG_ANOVA;
    class Source Discipline;
    model 'Dimension 2'n = Source Discipline Source*Discipline;
    means Source*Discipline;
run;
quit;

/* ANOVA - Dimension 3 by Source by Discipline */

title "ANOVA for &project - Dimension 3 by Source by Discipline";
ods noproctitle;
ods graphics / imagemap=on;

proc glm data=WORK.CL_ST4_PH1_EYAMROG_ANOVA;
    class Source Discipline;
    model 'Dimension 3'n = Source Discipline Source*Discipline;
    means Source*Discipline;
run;
quit;

/* ANOVA - Dimension 4 by Source by Discipline */

title "ANOVA for &project - Dimension 4 by Source by Discipline";
ods noproctitle;
ods graphics / imagemap=on;

proc glm data=WORK.CL_ST4_PH1_EYAMROG_ANOVA;
    class Source Discipline;
    model 'Dimension 4'n = Source Discipline Source*Discipline;
    means Source*Discipline;
run;
quit;

/* ANOVA - Dimension 5 by Source by Discipline */

title "ANOVA for &project - Dimension 5 by Source by Discipline";
ods noproctitle;
ods graphics / imagemap=on;

proc glm data=WORK.CL_ST4_PH1_EYAMROG_ANOVA;
    class Source Discipline;
    model 'Dimension 5'n = Source Discipline Source*Discipline;
    means Source*Discipline;
run;
quit;
