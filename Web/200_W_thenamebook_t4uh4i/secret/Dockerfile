FROM php:7.3-apache
WORKDIR /var/www/html/
COPY ./source .

ENV flag=f0rtn1ght{1s_iT_m3_0r_pr3p4red_stAt3MenT_Is_pl4y1ng_DumB?}

RUN touch db.db
RUN php init.php
RUN rm init.php

RUN chown -R www-data .