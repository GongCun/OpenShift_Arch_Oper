# This Dockerfile uses the rhel7 image
# Ahthor: Cun Gong
#FROM rhel7:v3
FROM puzzle:v3.0
COPY ./puzzler /puzzler
COPY ./run.sh /run.sh
COPY ./puzzle-entry.sh /puzzle-entry.sh
RUN chmod 755 puzzler run.sh puzzle-entry.sh && mkdir -p /data
EXPOSE 3001
CMD ["/puzzle-entry.sh"]

