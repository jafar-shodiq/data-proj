/*
 * Copyright (c) 2020 the original author or authors
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      https://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
 * or implied. See the License for the specific language governing
 * permissions and limitations under the License.
 */

package com.exadel.frs.core.trainservice.system.feign.python;

import com.fasterxml.jackson.annotation.JsonProperty;
import lombok.Data;
import lombok.experimental.Accessors;

@Data
@Accessors(chain = true)
public class ScanBox {

    @JsonProperty(value = "probability")
    private Double probability;

    @JsonProperty(value = "x_max")
    private Integer xMax;

    @JsonProperty(value = "y_max")
    private Integer yMax;

    @JsonProperty(value = "x_min")
    private Integer xMin;

    @JsonProperty(value = "y_min")
    private Integer yMin;
}
