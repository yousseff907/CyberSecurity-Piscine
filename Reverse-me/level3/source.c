/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   source.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: yitani <yitani@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/07 22:19:17 by yitani            #+#    #+#             */
/*   Updated: 2025/11/08 12:45:49 by yitani           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(void)
{
	char	input[24];
	char	buffer[10];

	memset(buffer, 0, 9);
	printf("please enter key: ");
	scanf("%23s", input);
	if (input[0] != '4' || input[1] != '2')
	{
		printf("Nope.\n");
		return (1);
	}
	int i = 2;
	int	buffer_index = 0;
	while (i < strlen(input) && i <= 23)
	{
		char three_digits[4] = {0};
		three_digits[0] = input[i];
		three_digits[1] = input[i + 1];
		three_digits[2] = input[i + 2];

		int	ascii_value = atoi(three_digits);
		buffer[buffer_index] = (char)ascii_value;
		buffer_index++;
		i += 3;
	}
	buffer[buffer_index] = '\0';
	if (strcmp(buffer, "*******") == 0)
		printf("Good job.\n");
	else
	{
		printf("Nope.\n");
		return (1);
	}
	
	return (0);
}