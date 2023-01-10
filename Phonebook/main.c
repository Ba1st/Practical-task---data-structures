#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define END (0)
#define MAX_LINE (4096)
#define ERROR (-1)

struct person;
typedef struct person* Position;

typedef struct person {
	char firstname[MAX_LINE];
	char lastname[MAX_LINE];
	char number[MAX_LINE];
	Position next;
}Person;

int AddPerson(Position);
int PrintList(Position);
int FindPersonByLastname(Position);
int FindPersonByFirstname(Position);
int DeletePerson(Position);
Position FindPrevious(Position, char *);
void Sortl(Position);
void Sortf(Position);

int main() {

	int n;

	Person head = {
		.firstname = {0},
		.lastname = {0},
		.number = 0,
		.next = NULL
	};

	while(1){

	printf("\nPlease insert a number of function you want to start: ");
	printf("\n1. Insert a person");
	printf("\n2. Print phonebook");
	printf("\n3. Find person by his lastname");
    printf("\n4. Find person by his firstname");
	printf("\n5. Delete person from the phonebook");
	printf("\n6. Exit");
	printf("\nAnswer: ");
	scanf("%d", &n);

	if (n == 1){
		AddPerson(&head);
        Sortf(&head);
        Sortl(&head);
    }

	else if (n == 2)
		PrintList(&head);

	else if (n == 3)
		FindPersonByLastname(&head);

    else if (n == 4)
		FindPersonByFirstname(&head);

	else if (n == 5)
		DeletePerson(&head);

    else if(n==6)
        break;

	else
		printf("\nWrong input!\n");

	printf("\n");

	}

	return END;
}


int AddPerson(Position P){

	Position q = NULL;

	q = (Position)malloc(sizeof(struct person));

	if (q == NULL)
		return ERROR;

	printf("\nEnter the person firstname, lastname and Number:  ");
	scanf(" %s %s %s", q->firstname, q->lastname, q->number);

	q->next = P->next;
	P->next = q;

	return END;
}

int PrintList(Position P) {

	if (P->next == NULL)
		printf("The phonebook is empty!");

	else {

		printf("\nContacs: ");

		while (P != NULL) {
			printf("\n%s %s %s", P->firstname, P->lastname, P->number);
			P = P->next;
		}
	}

	return END;
}

int FindPersonByLastname(Position P) {

	char lastname[MAX_LINE] = { 0 };

	printf("\nEnter the person lastname: ");
	scanf(" %s", lastname);

	while (P->next != NULL){
        if(strcmp(P->lastname, lastname) == 0){
            printf("%s %s %s\n", P->firstname, P->lastname, P->number);
        }
		P = P->next;
    }

    if(strcmp(P->lastname, lastname) == 0)
	    printf("%s %s %s", P->firstname, P->lastname, P->number);  
    
    else
        printf("\nPerson do not exist!");

	return END;
}

int FindPersonByFirstname(Position P) {

	char firstaname[MAX_LINE] = { 0 };

	printf("\nEnter the person firstname: ");
	scanf(" %s", firstaname);

	while (P->next != NULL){
        if(strcmp(P->firstname, firstaname) == 0){
            printf("%s %s %s\n", P->firstname, P->lastname, P->number);
        }
		P = P->next;
    }

    if(strcmp(P->firstname, firstaname) == 0)
	    printf("%s %s %s", P->firstname, P->lastname, P->number);

    else
        printf("\nPerson do not exist!");

	return END;
}


int DeletePerson(Position P) {

	char lastnm[MAX_LINE] = { 0 };

	printf("\nEnter the person lastname: ");
	scanf(" %s", lastnm);

	Position previous = NULL;
	Position Current = NULL;

	previous = FindPrevious(P,lastnm);

	if (previous == NULL)
		return ERROR;

	Current = previous->next;
	previous->next = previous->next->next;

	free(Current);

	return END;
}

Position FindPrevious(Position P, char* lastnm) {

	Position Previous = NULL;
	Position Current = NULL;

	Previous = P;
	Current = Previous->next;

	while (Current != NULL && (strcmp(lastnm,Current->lastname) != 0)) {

		Previous = Current;
		Current = Previous->next;
	}

	if (Current == NULL)
		return NULL;

	return Previous;
}


void Sortl(Position P) {
	Position j, prev_j, temp, end;

	end = NULL;

	while (P->next != end) {

		prev_j = P;
		j = P->next;

		while (j->next != end) {

			if (strcmp(j->lastname, j->next->lastname) > 0) {

				temp = j->next;
				prev_j->next = temp;
				j->next = temp->next;
				temp->next=j;

				j = temp;
			}

			prev_j = j;
			j = j->next;
		}

		end = j;
	}
}

void Sortf(Position P) {
	Position j, prev_j, temp, end;

	end = NULL;

	while (P->next != end) {

		prev_j = P;
		j = P->next;

		while (j->next != end) {

			if (strcmp(j->firstname, j->next->firstname) > 0) {

				temp = j->next;
				prev_j->next = temp;
				j->next = temp->next;
				temp->next=j;

				j = temp;
			}

			prev_j = j;
			j = j->next;
		}

		end = j;
	}
}